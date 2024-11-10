from flask import Flask, redirect, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_migrate import Migrate  # Import Flask-Migrate
from flask_cors import CORS

# Create the db instance globally
db = SQLAlchemy()

# Create the API instance globally
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Create the Migrate instance globally
migrate = Migrate()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Allow all origins (not recommended for production)
    CORS(app)

    # Load configuration based on environment
    app.config.from_object('config.DevelopmentConfig')  # Replace with `ProductionConfig` or `TestingConfig` as needed

    # Initialize db and api with the app
    db.init_app(app)
    api.init_app(app)

    # Initialize Flask-Migrate with the app and db
    migrate.init_app(app, db)

    # Swagger Setup
    swagger = Swagger(app, template_file='static/swagger.yaml')

    # Register the blueprint with the app
    app.register_blueprint(api_bp, url_prefix='/api')

    # Import routes here to avoid circular imports
    from api.routes.areas import AreaResource
    from api.routes.teams import TeamResource
    from api.routes.players import PlayerResource
    from api.routes.matches import MatchResource
    from api.routes.player_details import PlayerDetailResource

    # Register routes
    api.add_resource(AreaResource, '/areas')
    api.add_resource(TeamResource, '/teams')
    api.add_resource(PlayerResource, '/players')
    api.add_resource(MatchResource, '/matches')
    api.add_resource(PlayerDetailResource, '/players/<int:player_id>')

    # Root route for Swagger UI
    @app.route('/')
    def swagger_ui():
        return redirect('/apidocs')

    # Import all models to ensure they are loaded before creating tables
    from api.models.area import Area
    from api.models.team import Team   # Import the team model
    from api.models.player import Player  # Import the player model, if it's involved in relationships
    from api.models.match import Match  # Import the match model

    return app

# This block will ensure that the app runs when executed directly
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
