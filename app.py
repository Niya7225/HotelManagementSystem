from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hotel, Staff, Guest, RoomType, Room, Reservation, Billing, Payment, Service, Bill_Service

app = Flask(__name__)

# --- Database Configuration (UPDATE THIS WITH YOUR CREDENTIALS) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hotel_user:hotel_user:dbms123@192.168.114.194/hotel_management_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with your app
db.init_app(app)
migrate = Migrate(app, db)

# --- General Endpoint ---
@app.route('/')
def index():
    return "Hello, this is the Hotel Management System Backend!"

# --- Guest API Endpoints ---
@app.route('/api/guests', methods=['POST'])
def create_guest():
    try:
        data = request.json
        new_guest = Guest(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phoneNumber=data['phoneNumber'],
            idProof=data.get('idProof'),
            address=data.get('address')
        )
        db.session.add(new_guest)
        db.session.commit()
        return jsonify({"message": "Guest created successfully!", "guestID": new_guest.guestID}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/guests', methods=['GET'])
def get_all_guests():
    guests = Guest.query.all()
    output = []
    for guest in guests:
        guest_data = {
            'guestID': guest.guestID,
            'firstName': guest.firstName,
            'lastName': guest.lastName,
            'email': guest.email,
            'phoneNumber': guest.phoneNumber,
            'address': guest.address,
            'idProof': guest.idProof
        }
        output.append(guest_data)
    return jsonify({'guests': output})

@app.route('/api/guests/<int:guest_id>', methods=['GET'])
def get_guest_by_id(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'message': 'Guest not found'}), 404
    
    guest_data = {
        'guestID': guest.guestID,
        'firstName': guest.firstName,
        'lastName': guest.lastName,
        'email': guest.email,
        'phoneNumber': guest.phoneNumber,
        'address': guest.address,
        'idProof': guest.idProof
    }
    return jsonify(guest_data)

@app.route('/api/guests/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'message': 'Guest not found'}), 404
    
    data = request.json
    guest.firstName = data.get('firstName', guest.firstName)
    guest.lastName = data.get('lastName', guest.lastName)
    guest.email = data.get('email', guest.email)
    guest.phoneNumber = data.get('phoneNumber', guest.phoneNumber)
    guest.idProof = data.get('idProof', guest.idProof)
    guest.address = data.get('address', guest.address)
    db.session.commit()
    return jsonify({'message': 'Guest updated successfully!'})

@app.route('/api/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    guest = Guest.query.get(guest_id)
    if not guest:
        return jsonify({'message': 'Guest not found'}), 404
    
    db.session.delete(guest)
    db.session.commit()
    return jsonify({'message': 'Guest deleted successfully!'})

# --- Staff API Endpoints ---
@app.route('/api/staff', methods=['POST'])
def create_staff():
    try:
        data = request.json
        new_staff = Staff(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            phoneNumber=data['phoneNumber'],
            username=data['username'],
            passwordHash=data['passwordHash'],
            role=data['role'],
            address=data.get('address'),
            dateOfHire=data.get('dateOfHire'),
            salary=data.get('salary')
        )
        db.session.add(new_staff)
        db.session.commit()
        return jsonify({"message": "Staff member created successfully!", "staffID": new_staff.staffID}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/staff', methods=['GET'])
def get_all_staff():
    staff_members = Staff.query.all()
    output = []
    for staff in staff_members:
        staff_data = {
            'staffID': staff.staffID,
            'firstName': staff.firstName,
            'lastName': staff.lastName,
            'email': staff.email,
            'phoneNumber': staff.phoneNumber,
            'username': staff.username,
            'role': staff.role,
            'address': staff.address,
            'dateOfHire': str(staff.dateOfHire),
            'salary': str(staff.salary)
        }
        output.append(staff_data)
    return jsonify({'staff': output})

@app.route('/api/staff/<int:staff_id>', methods=['GET'])
def get_staff_by_id(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return jsonify({'message': 'Staff member not found'}), 404
    
    staff_data = {
        'staffID': staff.staffID,
        'firstName': staff.firstName,
        'lastName': staff.lastName,
        'email': staff.email,
        'phoneNumber': staff.phoneNumber,
        'username': staff.username,
        'role': staff.role,
        'address': staff.address,
        'dateOfHire': str(staff.dateOfHire),
        'salary': str(staff.salary)
    }
    return jsonify(staff_data)

@app.route('/api/staff/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return jsonify({'message': 'Staff member not found'}), 404
    
    data = request.json
    staff.firstName = data.get('firstName', staff.firstName)
    staff.lastName = data.get('lastName', staff.lastName)
    staff.email = data.get('email', staff.email)
    staff.phoneNumber = data.get('phoneNumber', staff.phoneNumber)
    staff.username = data.get('username', staff.username)
    staff.role = data.get('role', staff.role)
    staff.address = data.get('address', staff.address)
    staff.dateOfHire = data.get('dateOfHire', staff.dateOfHire)
    staff.salary = data.get('salary', staff.salary)
    db.session.commit()
    return jsonify({'message': 'Staff member updated successfully!'})

@app.route('/api/staff/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = Staff.query.get(staff_id)
    if not staff:
        return jsonify({'message': 'Staff member not found'}), 404
    
    db.session.delete(staff)
    db.session.commit()
    return jsonify({'message': 'Staff member deleted successfully!'})

# --- Room API Endpoints ---
@app.route('/api/rooms', methods=['POST'])
def add_room():
    data = request.json
    new_room = Room(
        roomNumber=data['roomNumber'],
        hotelID=data['hotelID'],
        roomTypeID=data['roomTypeID'],
        floorNumber=data['floorNumber'],
        currentStatus=data['currentStatus']
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify({"message": "Room added successfully!"}), 201

@app.route('/api/rooms', methods=['GET'])
def get_all_rooms():
    rooms = Room.query.all()
    output = []
    for room in rooms:
        output.append({
            'roomNumber': room.roomNumber,
            'hotelID': room.hotelID,
            'roomTypeID': room.roomTypeID,
            'floorNumber': room.floorNumber,
            'currentStatus': room.currentStatus
        })
    return jsonify({'rooms': output})

@app.route('/api/rooms/<int:room_number>', methods=['GET'])
def get_room(room_number):
    room = Room.query.get(room_number)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    
    room_data = {
        'roomNumber': room.roomNumber,
        'hotelID': room.hotelID,
        'roomTypeID': room.roomTypeID,
        'floorNumber': room.floorNumber,
        'currentStatus': room.currentStatus
    }
    return jsonify(room_data)

@app.route('/api/rooms/<int:room_number>', methods=['PUT'])
def update_room(room_number):
    room = Room.query.get(room_number)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    
    data = request.json
    room.hotelID = data.get('hotelID', room.hotelID)
    room.roomTypeID = data.get('roomTypeID', room.roomTypeID)
    room.floorNumber = data.get('floorNumber', room.floorNumber)
    room.currentStatus = data.get('currentStatus', room.currentStatus)
    db.session.commit()
    return jsonify({'message': 'Room updated successfully!'})

@app.route('/api/rooms/<int:room_number>', methods=['DELETE'])
def delete_room(room_number):
    room = Room.query.get(room_number)
    if not room:
        return jsonify({'message': 'Room not found'}), 404
    
    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted successfully!'})

# --- RoomType API Endpoints ---
@app.route('/api/room_types', methods=['POST'])
def add_room_type():
    data = request.json
    new_room_type = RoomType(
        typeName=data['typeName'],
        description=data.get('description'),
        basePrice=data['basePrice'],
        capacity=data['capacity']
    )
    db.session.add(new_room_type)
    db.session.commit()
    return jsonify({"message": "Room type added successfully!", "roomTypeID": new_room_type.roomTypeID}), 201

@app.route('/api/room_types', methods=['GET'])
def get_all_room_types():
    room_types = RoomType.query.all()
    output = []
    for room_type in room_types:
        output.append({
            'roomTypeID': room_type.roomTypeID,
            'typeName': room_type.typeName,
            'description': room_type.description,
            'basePrice': str(room_type.basePrice),
            'capacity': room_type.capacity
        })
    return jsonify({'room_types': output})

@app.route('/api/room_types/<int:room_type_id>', methods=['GET'])
def get_room_type(room_type_id):
    room_type = RoomType.query.get(room_type_id)
    if not room_type:
        return jsonify({'message': 'Room type not found'}), 404
    
    room_type_data = {
        'roomTypeID': room_type.roomTypeID,
        'typeName': room_type.typeName,
        'description': room_type.description,
        'basePrice': str(room_type.basePrice),
        'capacity': room_type.capacity
    }
    return jsonify(room_type_data)

@app.route('/api/room_types/<int:room_type_id>', methods=['PUT'])
def update_room_type(room_type_id):
    room_type = RoomType.query.get(room_type_id)
    if not room_type:
        return jsonify({'message': 'Room type not found'}), 404
    
    data = request.json
    room_type.typeName = data.get('typeName', room_type.typeName)
    room_type.description = data.get('description', room_type.description)
    room_type.basePrice = data.get('basePrice', room_type.basePrice)
    room_type.capacity = data.get('capacity', room_type.capacity)
    db.session.commit()
    return jsonify({'message': 'Room type updated successfully!'})

@app.route('/api/room_types/<int:room_type_id>', methods=['DELETE'])
def delete_room_type(room_type_id):
    room_type = RoomType.query.get(room_type_id)
    if not room_type:
        return jsonify({'message': 'Room type not found'}), 404
    
    db.session.delete(room_type)
    db.session.commit()
    return jsonify({'message': 'Room type deleted successfully!'})

# --- Service API Endpoints ---
@app.route('/api/services', methods=['POST'])
def add_service():
    data = request.json
    new_service = Service(
        serviceName=data['serviceName'],
        description=data.get('description'),
        unitPrice=data['unitPrice']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify({"message": "Service added successfully!", "serviceID": new_service.serviceID}), 201

@app.route('/api/services', methods=['GET'])
def get_all_services():
    services = Service.query.all()
    output = []
    for service in services:
        output.append({
            'serviceID': service.serviceID,
            'serviceName': service.serviceName,
            'description': service.description,
            'unitPrice': str(service.unitPrice)
        })
    return jsonify({'services': output})

@app.route('/api/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404
    
    service_data = {
        'serviceID': service.serviceID,
        'serviceName': service.serviceName,
        'description': service.description,
        'unitPrice': str(service.unitPrice)
    }
    return jsonify(service_data)

@app.route('/api/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404
    
    data = request.json
    service.serviceName = data.get('serviceName', service.serviceName)
    service.description = data.get('description', service.description)
    service.unitPrice = data.get('unitPrice', service.unitPrice)
    db.session.commit()
    return jsonify({'message': 'Service updated successfully!'})

@app.route('/api/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get(service_id)
    if not service:
        return jsonify({'message': 'Service not found'}), 404
    
    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully!'})


# --- Reservation API Endpoints (complex logic) ---
@app.route('/api/reservations', methods=['POST'])
def add_reservation():
    try:
        data = request.json
        # 1. You would add room availability check here
        
        new_reservation = Reservation(
            guestID=data['guestID'],
            roomNumber=data['roomNumber'],
            checkInDate=datetime.strptime(data['checkInDate'], '%Y-%m-%d').date(),
            checkOutDate=datetime.strptime(data['checkOutDate'], '%Y-%m-%d').date(),
            bookingDate=datetime.now(),
            numberOfAdults=data['numberOfAdults'],
            numberOfChildren=data['numberOfChildren'],
            reservationStatus='Confirmed',
            pricePerNight=data['pricePerNight']
        )
        db.session.add(new_reservation)
        db.session.commit()
        
        # Automatically create a billing record for the reservation
        new_billing = Billing(
            reservationID=new_reservation.reservationID,
            billDate=datetime.now(),
            paymentStatus='Pending'
        )
        db.session.add(new_billing)
        db.session.commit()
        
        return jsonify({"message": "Reservation created successfully!", "reservationID": new_reservation.reservationID}), 201

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations', methods=['GET'])
def get_all_reservations():
    reservations = Reservation.query.all()
    output = []
    for res in reservations:
        output.append({
            'reservationID': res.reservationID,
            'guestID': res.guestID,
            'roomNumber': res.roomNumber,
            'checkInDate': str(res.checkInDate),
            'checkOutDate': str(res.checkOutDate),
            'bookingDate': str(res.bookingDate),
            'numberOfAdults': res.numberOfAdults,
            'numberOfChildren': res.numberOfChildren,
            'reservationStatus': res.reservationStatus,
            'pricePerNight': str(res.pricePerNight)
        })
    return jsonify({'reservations': output})

@app.route('/api/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    
    reservation_data = {
        'reservationID': reservation.reservationID,
        'guestID': reservation.guestID,
        'roomNumber': reservation.roomNumber,
        'checkInDate': str(reservation.checkInDate),
        'checkOutDate': str(reservation.checkOutDate),
        'bookingDate': str(reservation.bookingDate),
        'numberOfAdults': reservation.numberOfAdults,
        'numberOfChildren': reservation.numberOfChildren,
        'reservationStatus': reservation.reservationStatus,
        'pricePerNight': str(reservation.pricePerNight)
    }
    return jsonify(reservation_data)

@app.route('/api/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    
    data = request.json
    reservation.guestID = data.get('guestID', reservation.guestID)
    reservation.roomNumber = data.get('roomNumber', reservation.roomNumber)
    reservation.checkInDate = data.get('checkInDate', reservation.checkInDate)
    reservation.checkOutDate = data.get('checkOutDate', reservation.checkOutDate)
    db.session.commit()
    return jsonify({'message': 'Reservation updated successfully!'})

@app.route('/api/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    if not reservation:
        return jsonify({'message': 'Reservation not found'}), 404
    
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation deleted successfully!'})

# --- Billing API Endpoints ---
@app.route('/api/billings', methods=['GET'])
def get_all_billings():
    billings = Billing.query.all()
    output = []
    for bill in billings:
        output.append({
            'billID': bill.billID,
            'reservationID': bill.reservationID,
            'billDate': str(bill.billDate),
            'subTotal': str(bill.subTotal),
            'taxAmount': str(bill.taxAmount),
            'totalAmount': str(bill.totalAmount),
            'paymentStatus': bill.paymentStatus
        })
    return jsonify({'billings': output})

@app.route('/api/billings/<int:bill_id>', methods=['GET'])
def get_billing_by_id(bill_id):
    billing = Billing.query.get(bill_id)
    if not billing:
        return jsonify({'message': 'Billing record not found'}), 404
    
    billing_data = {
        'billID': billing.billID,
        'reservationID': billing.reservationID,
        'billDate': str(billing.billDate),
        'subTotal': str(billing.subTotal),
        'taxAmount': str(billing.taxAmount),
        'totalAmount': str(billing.totalAmount),
        'paymentStatus': billing.paymentStatus
    }
    return jsonify(billing_data)

# --- Payment API Endpoints ---
@app.route('/api/payments', methods=['POST'])
def add_payment():
    data = request.json
    new_payment = Payment(
        billID=data['billID'],
        paymentMethod=data['paymentMethod'],
        paymentDate=datetime.now(),
        amountPaid=data['amountPaid'],
        transactionID=data.get('transactionID')
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment added successfully!", "paymentID": new_payment.paymentID}), 201

@app.route('/api/payments', methods=['GET'])
def get_all_payments():
    payments = Payment.query.all()
    output = []
    for payment in payments:
        output.append({
            'paymentID': payment.paymentID,
            'billID': payment.billID,
            'paymentMethod': payment.paymentMethod,
            'paymentDate': str(payment.paymentDate),
            'amountPaid': str(payment.amountPaid),
            'transactionID': payment.transactionID
        })
    return jsonify({'payments': output})

@app.route('/api/payments/<int:payment_id>', methods=['GET'])
def get_payment_by_id(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    
    payment_data = {
        'paymentID': payment.paymentID,
        'billID': payment.billID,
        'paymentMethod': payment.paymentMethod,
        'paymentDate': str(payment.paymentDate),
        'amountPaid': str(payment.amountPaid),
        'transactionID': payment.transactionID
    }
    return jsonify(payment_data)

if __name__ == '__main__':
    app.run(debug=True)