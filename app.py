from flask import Flask
from routes.inventory import inventory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://usuario1:usuario6@localhost/inventory_db'
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(inventory)