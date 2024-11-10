from flask_restful import Resource
from api.models.team import Team
from api.app import db
from flask import current_app, request, jsonify

class TeamResource(Resource):
    def get(self):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search_query = request.args.get('search', '', type=str)

        teams_query = Team.query.filter(Team.name.ilike(f'%{search_query}%'))  # Filter teams based on search query
        teams_paginated = teams_query.paginate(page=page, per_page=per_page, error_out=False)

        teams = [{'id': team.id, 'name': team.name, 'logo_url': team.logo_url} for team in teams_paginated.items]
        total_pages = teams_paginated.pages

        return jsonify({'teams': teams, 'totalPages': total_pages, 'currentPage': page})
    
    def post(self):
        request_data = request.get_json()
        if not request_data:
            return {'message': "'teams' key is missing in the request body"}, 400
        
        teams_data = request_data['teams']

        # Get MAX_ITEMS value from the configuration
        max_items = current_app.config['MAX_ITEMS']

        # Check if we exceed the max limit
        if len(teams_data) > max_items:
            return {'message': f"You can only add up to {max_items} matches at once."}, 400
        
        teams = []
        
        for team_data in teams_data:
            if 'name' not in team_data or 'logo_url' not in team_data:
                return {'message': "Missing required fields in one of the team records"}, 400
            team = Team(
                name=team_data['name'],
                country=team_data.get('country', None),
                logo_url=team_data['logo_url']
            )
            teams.append(team)

        db.session.bulk_save_objects(teams)
        db.session.commit()

        return {'message': f'{len(teams)} teams created'}, 201
