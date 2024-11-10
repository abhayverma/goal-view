from flask_restful import Resource
from api.models.area import Area
from api.app import db
from flask import current_app, request

class AreaResource(Resource):
    def get(self):
        areas = Area.query.all()
        return {'areas': [area.serialize() for area in areas]}
    
    def post(self):
        request_data = request.get_json()
        if not request_data or 'areas' not in request_data:
            return {'message': "'areas' key is missing in the request body"}, 400 
        
        areas_data = request_data['areas']

        # Get MAX_ITEMS value from the configuration
        max_items = current_app.config['MAX_ITEMS']

        # Check if we exceed the max limit
        if len(areas_data) > max_items:
            return {'message': f"You can only add up to {max_items} matches at once."}, 400
        
        areas = []

        for area_data in areas_data:
            required_fields = ['name', 'state', 'country']
            if not all(field in area_data for field in required_fields):
                missing_fields = [field for field in required_fields if field not in area_data]
                return {'message': f"Missing required fields: {', '.join(missing_fields)}"}, 400
            area = Area(
                name=area_data['name'],
                state=area_data['state'],
                country=area_data['country'],
                description=area_data.get('description', None)
                )
            areas.append(area)

        db.session.bulk_save_objects(areas)
        db.session.commit()

        return {'message': f'{len(areas)} areas created'}, 201
