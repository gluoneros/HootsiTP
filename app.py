from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario1:usuario6@localhost/inventory_db'
db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(17), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Inventory(id={self.id}, name={self.name}, price={self.price}, mac_address={self.mac_address}, serial_number={self.serial_number}, manufacturer={self.manufacturer}, description={self.description})"

#@app.route("/")
#def home():
#    return "hello"    

@app.route('/Inventory', methods=['GET', 'POST'])
def handle_inventory():
    if request.method == 'POST':
        data = request.json
        new_item = Inventory(
            name=data['name'],
            price=data['price'],
            mac_address=data['mac_address'],
            serial_number=data['serial_number'],
            manufacturer=data['manufacturer'],
            description=data.get('description')
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item added successfully"}), 201
    elif request.method == 'GET':
        inventory_items = Inventory.query.all()
        result = [
            {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "mac_address": item.mac_address,
                "serial_number": item.serial_number,
                "manufacturer": item.manufacturer,
                "description": item.description
            } for item in inventory_items
        ]
        return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True)