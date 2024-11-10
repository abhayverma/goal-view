from api.app import db

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100))
    logo_url = db.Column(db.String(255))

    # A team can have multiple players
    players = db.relationship('Player', back_populates='team')

    # A team can have multiple home matches (where this team is the home team)
    home_matches = db.relationship('Match', foreign_keys='Match.home_team_id', back_populates='home_team')

    # A team can have multiple away matches (where this team is the away team)
    away_matches = db.relationship('Match', foreign_keys='Match.away_team_id', back_populates='away_team')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'logo_url': self.logo_url,
            'players': [{'name': player.name, 'position': player.position.value if player.position else None} for player in self.players],
            'home_matches': [home_match.serialize() for home_match in self.home_matches],
            'away_matches': [away_match.serialize() for away_match in self.away_matches]
        }