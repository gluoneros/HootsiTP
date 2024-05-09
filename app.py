from flask import Flask
from routes.inventory import inventory

app = Flask(__name__)


app.register_blueprint(inventory)