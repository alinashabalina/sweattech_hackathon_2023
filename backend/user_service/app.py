from flask import Flask, jsonify
from flask_migrate import Migrate

from models import init_app, db

app = Flask(__name__)

GROUPS_URL = "http://127.0.0.1:5001"

app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    response = {"message": "This page is empty"}
    return jsonify(response), 200