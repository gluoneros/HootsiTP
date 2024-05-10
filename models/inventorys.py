from utils.db import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(255))
    price = db.Column(db.Integer)
    mac_address = db.Column(db.string(255))
    serial_number = db.Column(db.string(255))
    manufacturer = db.Column(db.string(255))
    description = db.Column(db.string(255))

    def __init__(self, name, price, mac_address, serial_number, manufacturer, description):
        self.name = name
        self.price = price
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        self.description = description