from flask import Blueprint, render_template
#from flask import Blueprint
from flask import request, jsonify
#from app import app, db, Inventory

inventory = Blueprint('inventory', __name__)

@inventory.route('/')
def shows():
    inventory = Inventory.query.all()
    return render_template('index.html', inventory=inventory)

@inventory.route('/add')
def add():
    return render_template('add.html')

@inventory.route('/edit')
def edit():
    return 'Edits an existing item using its ID'

@inventory.route('/delete')
def delete():
    return 'Deletes an item using its ID'