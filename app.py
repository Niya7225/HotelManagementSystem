from flask import Flask, request, jsonify
from models import db, Guest, Room, Reservation, Staff, RoomType, Billing, Payment, Service, Bill_Service

app = Flask(__name__)

# The database config and db.init_app will be added later
# once your teammate gives you the credentials.

# --- Your API Endpoints Go Here ---

# Example: A simple "Hello, World!" to test the server
@app.route('/')
def index():
    return "Hello, this is the Hotel Management System Backend!"

# Example: A placeholder for your Guest API endpoint
@app.route('/api/guests', methods=['POST'])
def create_guest():
    # You will add the logic to save a guest here later
    return "This endpoint is a work in progress!"

# --- End of API Endpoints ---

if __name__ == '__main__':
    app.run(debug=True)