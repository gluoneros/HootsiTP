from flask import Blueprint, render_template
from flask import request, jsonify
#from app import *

inventory = Blueprint('inventory', __name__)

#@inventory.route('/')
#def show_inventory():
#    inventory_items = inventory.query.all()
#    return render_template('index.html', inventory_items=inventory_items)

@inventory.route('/add')
def add():
    return render_template('add.html')

@inventory.route('/edit')
def edit():
    return 'Edits an existing item using its ID'

@inventory.route('/delete')
def delete():
    return 'Deletes an item using its ID'