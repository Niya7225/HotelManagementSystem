from flask import Flask, request, jsonify
from flask_migrate import Migrate  # IMPORT THIS LINE
from models import db, Hotel, Staff, Guest, RoomType, Room, Reservation, Billing, Payment, Service, Bill_Service

app = Flask(__name__)

# --- Database Configuration (UPDATE THIS WITH YOUR CREDENTIALS) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hotel_user:dbms@123@192.168.114.194/hotel_management_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with your app
db.init_app(app)

# INITIALIZE FLASK-MIGRATE HERE
migrate = Migrate(app, db) # ADD THIS LINE

# --- Your API Endpoints Go Here ---

# A simple endpoint to test if the server is running
@app.route('/')
def index():
    return "Hello, this is the Hotel Management System Backend!"

# A placeholder endpoint for creating a new Guest
@app.route('/api/guests', methods=['POST'])
def create_guest():
    # You will add the logic to save a guest here later,
    # once you have tested the database connection.
    return "This endpoint is a work in progress!"

# --- End of API Endpoints ---

if __name__ == '__main__':
    app.run(debug=True)