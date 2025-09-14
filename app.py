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
# This should be a separate endpoint from your API logic
@app.route('/')
def index():
    return "Hello, this is the Hotel Management System Backend!"

# The "listener" for a POST request at this URL
@app.route('/api/guests', methods=['POST'])
def create_guest():
    try:
        data = request.json
        
        # 2. Create a new Python object that represents a new row in the Guest table
        new_guest = Guest(
            firstName=data.get('firstName'),  # Use .get() to avoid KeyError
            lastName=data.get('lastName'),
            email=data.get('email'),
            phoneNumber=data.get('phoneNumber'),
            idProof=data.get('idProof'),
            address=data.get('address')
        )

        # 3. Stage the new object to be saved to the database
        db.session.add(new_guest)

        # 4. Commit the changes, permanently saving the data
        db.session.commit()

        # 5. Return a success message and the new guest's ID
        return jsonify({"message": "Guest created successfully!", "guestID": new_guest.guestID}), 201
    
    except KeyError as e:
        # This catch is now less necessary but still good to have.
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        # Handles any other unexpected errors and reverts the changes
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# --- End of API Endpoints ---

if __name__ == '__main__':
    app.run(debug=True)