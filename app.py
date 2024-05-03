import os
import time

from flask import Flask

from models import init_app as db_init_app
from resources import init_app as api_init_app


app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/add')
def add():
    return app.send_static_file('add.html')


@app.route('/recipe')
def recipe_by_id():
    return app.send_static_file('recipe.html')


# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

# initialize database
db_init_app(app)

# initialization app to api
api_init_app(app)
