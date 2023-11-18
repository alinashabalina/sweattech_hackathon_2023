from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))

    def user_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }


class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    username = db.Column(db.String(255))
    date_of_birth = db.Column(db.String)
    hormone_state = db.Column(db.String(255))
    day_of_cycle = db.Column(db.Integer)
    goal_list = db.Column(db.String(255))

    def user_questionnaire(self):
        return {
            "id": self.id,
            "username": self.username,
            "date_of_birth": self.date_of_birth,
            "hormone_state": self.hormone_state,
            "day_of_cycle": self.day_of_cycle,
            "goal_list": self.goal_list,
        }


class DayView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    user_id = db.Column(db.Integer)
    day_energy = db.Column(db.String(255))
    period_day_correct = db.Column(db.Boolean)
    training_type = db.Column(db.String(255))
    feedback = db.Column(db.String(255))

    def day_info(self):
        return {
            "id": self.id,
            "date": self.date,
            "user_id": self.user_id,
            "day_energy": self.day_energy,
            "period_day_correct": self.period_day_correct,
            "training_type": self.training_type,
            "feedback": self.feedback
        }


class Trainings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    energy_level = db.Column(db.String(255))
    link = db.Column(db.String)

    def training_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "energy_level": self.energy_level,
            "link": self.link
        }


class TrainingRecommendations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def training_recommended(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "training_id": self.training_id
        }