from flask import Flask, render_template, request
from models import db, Reservation
import os
import logging
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'parking_reservation.db')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve-space', methods=['POST'])
def reserve_parking_space():
    try:
        reservation = Reservation(
            name = request.form['name'], 
            licensePlate = request.form['licensePlate'], 
            startDate = datetime.strptime(request.form['startDate'], '%Y-%m-%d'), 
            endDate = datetime.strptime(request.form['endDate'], '%Y-%m-%d'),
            parkingSpace = request.form['parkingSpace']
        )

        db.session.add(reservation)
        db.session.commit()

        reservationId = reservation.id

        return render_template('reservation-completed.html', name = reservation.name, reservation_id = reservationId)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return 'An error occurred while processing the reservation.'
    
if __name__ == '__main__':
    app.run(debug=True)