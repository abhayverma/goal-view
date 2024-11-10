from api.app import db

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    # Define the relationship with Match if applicable
    matches = db.relationship('Match', back_populates='area')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'state': self.state,
            'description': self.description,
            'matches': [match.serialize_simple() for match in self.matches]
        }