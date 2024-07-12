from flask import Blueprint, render_template
from flask import request, jsonify
from models.inventorys import *

inventory = Blueprint('inventory', __name__)

#@inventory.route('/')
#def show_inventory():
#    inventory_items = Inventory.query.all()
#    return render_template('index.html', inventory_items=inventory_items)

@inventory.route('/add')
def add():
    return render_template('add.html')

@inventory.route('/edit')
def edit():
    return 'Edits an existing item using its ID'

@inventory.route('/delete/<id>')
def delete(id):
    inventory = Inventory.query.get(id)
    print(inventory)
    db.session.delete(inventory)
    db.session.commit()
    return 'Deletes an item using its ID'