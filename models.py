from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --- Core Entities ---

class Hotel(db.Model):
    __tablename__ = 'hotel'
    hotelID = db.Column(db.Integer, primary_key=True)
    hotelName = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(255))
    contactEmail = db.Column(db.String(120), unique=True, nullable=False)
    contactPhone = db.Column(db.String(20))
    
class Staff(db.Model):
    __tablename__ = 'staff'
    staffID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    passwordHash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50))
    address = db.Column(db.String(255))
    dateOfHire = db.Column(db.Date)
    salary = db.Column(db.Numeric(10, 2))

class Guest(db.Model):
    __tablename__ = 'guest'
    guestID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(255))
    idProof = db.Column(db.String(100))

class RoomType(db.Model):
    __tablename__ = 'room_type'
    roomTypeID = db.Column(db.Integer, primary_key=True)
    typeName = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    basePrice = db.Column(db.Numeric(10, 2), nullable=False)
    capacity = db.Column(db.Integer)

class Room(db.Model):
    __tablename__ = 'room'
    roomNumber = db.Column(db.Integer, primary_key=True)
    hotelID = db.Column(db.Integer, db.ForeignKey('hotel.hotelID'))
    roomTypeID = db.Column(db.Integer, db.ForeignKey('room_type.roomTypeID'))
    floorNumber = db.Column(db.Integer)
    currentStatus = db.Column(db.String(20))

class Reservation(db.Model):
    __tablename__ = 'reservation'
    reservationID = db.Column(db.Integer, primary_key=True)
    guestID = db.Column(db.Integer, db.ForeignKey('guest.guestID'))
    roomNumber = db.Column(db.Integer, db.ForeignKey('room.roomNumber'))
    checkInDate = db.Column(db.Date)
    checkOutDate = db.Column(db.Date)
    bookingDate = db.Column(db.Date)
    numberOfAdults = db.Column(db.Integer)
    numberOfChildren = db.Column(db.Integer)
    reservationStatus = db.Column(db.String(20))
    pricePerNight = db.Column(db.Numeric(10, 2))

class Billing(db.Model):
    __tablename__ = 'billing'
    billID = db.Column(db.Integer, primary_key=True)
    reservationID = db.Column(db.Integer, db.ForeignKey('reservation.reservationID'), unique=True)
    billDate = db.Column(db.Date)
    subTotal = db.Column(db.Numeric(10, 2))
    taxAmount = db.Column(db.Numeric(10, 2))
    totalAmount = db.Column(db.Numeric(10, 2))
    paymentStatus = db.Column(db.String(20))

class Payment(db.Model):
    __tablename__ = 'payment'
    paymentID = db.Column(db.Integer, primary_key=True)
    billID = db.Column(db.Integer, db.ForeignKey('billing.billID'))
    paymentMethod = db.Column(db.String(50))
    paymentDate = db.Column(db.Date)
    amountPaid = db.Column(db.Numeric(10, 2))
    transactionID = db.Column(db.String(100))

class Service(db.Model):
    __tablename__ = 'service'
    serviceID = db.Column(db.Integer, primary_key=True)
    serviceName = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    unitPrice = db.Column(db.Numeric(10, 2))

class Bill_Service(db.Model):
    __tablename__ = 'bill_service'
    billServiceID = db.Column(db.Integer, primary_key=True)
    billID = db.Column(db.Integer, db.ForeignKey('billing.billID'))
    serviceID = db.Column(db.Integer, db.ForeignKey('service.serviceID'))
    quantity = db.Column(db.Integer)
    totalServicePrice = db.Column(db.Numeric(10, 2))
    