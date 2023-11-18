import json

import jsonschema
import sqlalchemy
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from sqlalchemy import select

from models import init_app, db, DayView, Trainings, TrainingRecommendations, User
from schemas import ValidationSchemas

app = Flask(__name__)

app.config['SECRET_KEY'] = "opop"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/day.db'
init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index_page():
    response = {"message": "This page is empty"}
    return jsonify(response), 200


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


@app.route("/day/create", methods=["POST"])
def set_a_day():
    try:
        day_view = DayView()
        jsonschema.validate(instance=json.loads(request.data), schema=ValidationSchemas.DayCreateSchema)
        day_view.user_id = json.loads(request.data)["user_id"]
        day_view.date = json.loads(request.data)["date"]
        day_view.day_energy = json.loads(request.data)["day_energy"]
        day_view.period_day_correct = json.loads(request.data)["period_day_correct"]
        day_view.training_type = json.loads(request.data)["training_type"]
        if "feedback" not in json.loads(request.data).keys():
            day_view.period_day_set = "not yet set"
        db.session.add(day_view)
        db.session.commit()
        response = {"message": "Day successfully set", "result": day_view.day_info()}
        return jsonify(response), 201
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


@app.route("/day/info/<user_id>/<date>", methods=["GET"])
def get_user_day(user_id, date):
    try:
        day_select = db.session.execute(select(DayView).filter_by(user_id=user_id).filter_by(date=date))
        day_selected = next(day_select)[0]
        response = {
            "message": "Info successfully acquired",
            "result": day_selected.day_info()
        }
        return jsonify(response), 200
    except StopIteration:
        response = {
            "message": "Oops something went wrong",
        }
        return jsonify(response), 400


@app.route("/training/create", methods=["POST"])
def post_a_training():
    try:
        training = Trainings()
        training.name = json.loads(request.data)["name"]
        training.energy_level = json.loads(request.data)["energy_level"]
        training.link = json.loads(request.data)["link"]
        db.session.add(training)
        db.session.commit()
        response = {"message": "Day successfully set", "result": training.training_info()}
        return jsonify(response), 201
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


@app.route("/day/recommend/<user_id>/<date>", methods=["GET"])
def recommend_user_training(user_id, date):
    try:
        day_select = db.session.execute(select(DayView).filter_by(user_id=user_id).filter_by(date=date))
        day_select = next(day_select)[0]
        training = db.session.execute(select(Trainings).filter_by(energy_level=day_select.day_info()["day_energy"]))
        training = next(training)[0]
        recommendation = TrainingRecommendations()
        recommendation.training_id = training.training_info()["id"]
        recommendation.user_id = user_id
        db.session.add(recommendation)
        db.session.commit()
        response = {
            "message": "Info successfully acquired",
            "result": training.training_info()
        }
        return jsonify(response), 200
    except StopIteration:
        response = {
            "message": "The training you're looking for is missing",
        }
        return jsonify(response), 400
