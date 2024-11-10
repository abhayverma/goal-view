from flask_restful import Resource
from api.models.match import Match
from api.app import db
from datetime import datetime
from flask import current_app, request

class MatchResource(Resource):
    def get(self):
        matches = Match.query.all()
        return {'matches': [match.serialize() for match in matches]}
    
    def post(self):
        request_data = request.get_json()
        if not request_data or 'matches' not in request_data:
            return {'message': "'matches' key is missing in the request body"}, 400
          
        matches_data = request_data['matches']
        
        # Get MAX_ITEMS value from the configuration
        max_items = current_app.config['MAX_ITEMS']

        # Check if we exceed the max limit
        if len(matches_data) > max_items:
            return {'message': f"You can only add up to {max_items} matches at once."}, 400
            
        matches = []
        
        for match_data in matches_data:
            required_fields = ['name', 'date', 'location', 'area_id', 'home_team_id', 'away_team_id']
            if not all(field in match_data for field in required_fields):
                return {'message': "Missing required fields in one of the match records"}, 400
            try:
                match_date = datetime.strptime(match_data['date'], '%Y-%m-%d')
            except ValueError:
                return {'message': "Invalid date format. Expected format: YYYY-MM-DD"}, 400
            match = Match(
                name=match_data['name'],
                date=match_data['date'],
                location=match_data['location'],
                area_id=match_data['area_id'],
                home_team_id=match_data['home_team_id'],
                away_team_id=match_data['away_team_id']
            )
            matches.append(match)

        db.session.bulk_save_objects(matches)
        db.session.commit()

        return {'message': f'{len(matches)} matches created'}, 201
