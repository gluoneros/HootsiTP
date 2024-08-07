from utils.db import db
#from app import *

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(17), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"Inventory(id={self.id}, name={self.name}, price={self.price}, mac_address={self.mac_address}, serial_number={self.serial_number}, manufacturer={self.manufacturer}, description={self.description})"
