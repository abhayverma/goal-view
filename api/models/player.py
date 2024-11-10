from api.app import db
from enum import Enum

# Enum for Player Position
class PlayerPosition(Enum):
    FORWARD = 'Forward'
    MIDFIELDER = 'Midfielder'
    DEFENDER = 'Defender'
    GOALKEEPER = 'Goalkeeper'

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.Enum(PlayerPosition), nullable=False)
    birthdate = db.Column(db.String(50))
    photo_url = db.Column(db.String(255), nullable=False)

    # Foreign key to reference the Team
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

    # Relationship with Team (each player belongs to one team)
    team = db.relationship('Team', back_populates='players')

    def serialize(self, nested=True):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position.value,
            'birthdate': self.birthdate,
            'team': self.team.serialize() if self.team and nested else None
        }