from api.app import db

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))  # Foreign key to Area

    # Relationships to Teams
    area = db.relationship('Area', foreign_keys=[area_id], back_populates='matches')
    home_team = db.relationship('Team', foreign_keys=[home_team_id], back_populates='home_matches')
    away_team = db.relationship('Team', foreign_keys=[away_team_id], back_populates='away_matches')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'location': self.location,
            'home_team_id': self.home_team_id,
            'away_team_id': self.away_team_id,
            'area': self.serialize_area()
        }
    
    def serialize_area(self):
        # Only include necessary fields of the area to prevent full recursion
        if self.area:
            return {
                'id': self.area.id,
                'name': self.area.name,
                'country': self.area.country,
                'state': self.area.state
            }
        return None
    
    def serialize_simple(self):
        # A simplified version of serialization to avoid recursion
        return {
            'id': self.id,
            'name': self.name
        }