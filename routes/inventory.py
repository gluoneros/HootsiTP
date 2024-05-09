from flask import Blueprint, render_template

inventory = Blueprint('inventory', __name__)

@inventory.route('/')
def shows():
    return render_template('index.html')

@inventory.route('/add')
def add():
    return 'Adds a new item to the database.'

@inventory.route('/edit')
def edit():
    return 'Edits an existing item using its ID'

@inventory.route('/delete')
def delete():
    return 'Deletes an item using its ID'