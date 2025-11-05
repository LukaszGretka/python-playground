from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    licensePlate  = db.Column(db.String(50), nullable=False)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=False)
    parkingSpace = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Reservation {self.name}>'