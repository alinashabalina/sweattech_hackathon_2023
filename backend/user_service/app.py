import json
import jsonschema
import sqlalchemy

from flask_migrate import Migrate
from flask import Flask, jsonify, request
from sqlalchemy import select

from models import init_app, db, User
from schemas import ValidationSchemas

app = Flask(__name__)

app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/user.db'
init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index_page():
    response = {"message": "This page is empty"}
    return jsonify(response), 200

@app.route("/unlogged")
def unlogged():
    response = {"message": "Please log in"}
    return jsonify(response), 400

@app.route("/create", methods=["POST"])
def create_user():
    try:
        user = User()
        jsonschema.validate(instance=json.loads(request.data), schema=ValidationSchemas.UserCreateSchema)
        user.email = json.loads(request.data)["email"]
        user.password = json.loads(request.data)["password"]
        if "username" not in json.loads(request.data).keys():
            user.username = ""
        else:
            user.username = json.loads(request.data)["username"]
        db.session.add(user)
        db.session.commit()
        response = {"message": "User created", "result": user.user_info()}
        return jsonify(response), 201
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        result = db.session.execute(select(User).filter_by(email=json.loads(request.data)["email"]))
        response = {
            "message": f"This user already exists",
        }
        return jsonify(response), 400
    except KeyError as e:
        db.session.rollback()
        if len(e.args) != 0:
            response = {
                "message": f"Make sure you have filled the {e.args[0]} field",
            }
        else:
            response = {
                "message": "Oops something went wrong. Check that all the fields are filled",
            }
        return jsonify(response), 400
    except jsonschema.exceptions.SchemaError as e:
        db.session.rollback()
        response = {
            "message": f"Check that all the fields are filled {e.json_path}",
        }
        return jsonify(response), 400
    except jsonschema.exceptions.ValidationError as e:
        db.session.rollback()
        response = {
            "message": f"Validation error: {e.message}",
        }
        return jsonify(response), 400