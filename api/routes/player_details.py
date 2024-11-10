from flask_restful import Resource
from api.models.player import Player
from flask import jsonify

class PlayerDetailResource(Resource):
    # Get details of a specific player by player_id
    def get(self, player_id):
        # Fetch the player by ID
        player = Player.query.get(player_id)

        if player is None:
            return {'message': 'Player not found'}, 404

        # Serialize the player details into a dictionary
        player_data = {
            'id': player.id,
            'name': player.name,
            'position': player.position.name if player.position else None,  # Convert Enum to string
            'photo_url': player.photo_url,
            'team_id': player.team_id
        }

        return jsonify(player_data)