# Import all models to ensure they are registered with SQLAlchemy
from .team import Team
from .player import Player
from .area import Area
from .match import Match
# Now all models are imported, and SQLAlchemy should be able to resolve relationships
