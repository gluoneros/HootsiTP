from flask import Blueprint, render_template
#from flask import Blueprint
from flask import request, jsonify
#from app import app, db, Inventory

inventory = Blueprint('inventory', __name__)

@inventory.route('/')
def shows():
    return render_template('index.html')

@inventory.route('/add', methods=['GET', 'POST'])
def add():
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

@inventory.route('/edit')
def edit():
    return 'Edits an existing item using its ID'

@inventory.route('/delete')
def delete():
    return 'Deletes an item using its ID'