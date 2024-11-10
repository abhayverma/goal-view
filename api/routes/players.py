from flask_restful import Resource
from api.models.player import Player, PlayerPosition
from api.app import db
from flask import current_app, request, jsonify

class PlayerResource(Resource):
    def get(self):
        team_id = request.args.get('teamId', type=int)
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search_query = request.args.get('search', '', type=str)

        players_query = Player.query.filter(Player.team_id == team_id, Player.name.ilike(f'%{search_query}%'))
        players_paginated = players_query.paginate(page=page, per_page=per_page, error_out=False)

        players = [{
            'id': player.id, 
            'name': player.name, 
            'position': player.position.name if player.position else None, 
            'photo_url': player.photo_url
        } for player in players_paginated.items]
        total_pages = players_paginated.pages

        return jsonify({'players': players, 'totalPages': total_pages, 'currentPage': page})
    
    
    def post(self):
        request_data = request.get_json()
        if not request_data or 'players' not in request_data:
            return {'message': "'players' key is missing in the request body"}, 400
        
        players_data = request_data['players']

        # Get MAX_ITEMS value from the configuration
        max_items = current_app.config['MAX_ITEMS']

        # Check if we exceed the max limit
        if len(players_data) > max_items:
            return {'message': f"You can only add up to {max_items} matches at once."}, 400
        
        players = []

        for player_data in players_data:
            if 'name' not in player_data or 'photo_url' not in player_data or 'team_id' not in player_data:
                return {'message': "Missing required fields in one of the player records"}, 400

            position = None
            if 'position' in player_data:
                try:
                    position = PlayerPosition[player_data['position'].upper()]  # Convert to Enum
                except KeyError:
                    return {'message': f"Invalid position. Valid positions are: {[pos.name for pos in PlayerPosition]}."}, 400
            
            player = Player(
                name=player_data['name'],
                position=position,
                photo_url=player_data['photo_url'],
                team_id=player_data['team_id']
            )
            players.append(player)

        db.session.bulk_save_objects(players)
        db.session.commit()

        return {'message': f'{len(players)} players created'}, 201
