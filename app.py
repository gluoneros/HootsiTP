from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from routes.routes import *
from models.inventorys import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario1:usuario6@localhost/inventory_db'
db = SQLAlchemy(app)

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


@app.route('/additem', methods=['GET', 'POST'])
def additem():
    if request.method == 'POST':
        data = request.form
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
        #return jsonify({"message": "Item added successfully"}), 201
        return redirect('/add')
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
    #return redirect('/add')

app.register_blueprint(inventory)

with app.app_context():
    db.create_all()

@app.route('/')
def show_inventory():
    inventory_items = Inventory.query.all()
    return render_template('index.html', inventory_items=inventory_items)

@app.route('/delete', methods=['GET'])
def show_delete_inventory():
    inventory_items = Inventory.query.all()
    return render_template('delete.html', inventory_items=inventory_items)

@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    item = Inventory.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": f"Item with id {item_id} deleted successfully"}), 200

@app.route('/edit', methods=['GET'])
def show_edit_item():
    inventory_items = Inventory.query.all()
    return render_template('edit.html', inventory_items=inventory_items)

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Inventory.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.price = request.form['price']
        item.mac_address = request.form['mac_address']
        item.serial_number = request.form['serial_number']
        item.manufacturer = request.form['manufacturer']
        item.description = request.form['description']
        db.session.commit()
        return jsonify({"message": f"Item with id {item_id} updated successfully"}), 200
    return render_template('edit_item.html', item=item)


if __name__ == '__main__':
    app.run(debug=True)