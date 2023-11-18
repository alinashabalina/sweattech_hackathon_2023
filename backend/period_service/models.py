from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class DayView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    day_energy = db.Column(db.String(255))
    period_day_correct = db.Column(db.Boolean)
    period_day_set = db.Column(db.Integer)
    training_type = db.Column(db.String(255))
    feedback = db.Column(db.String(255))

    def day_info(self):
        return {
            "id": self.id,
            "day_id": self.day_id,
            "user_id": self.user_id,
            "day_energy": self.day_energy,
            "period_day_correct": self.period_day_correct,
            "period_day_set": self.period_day_set,
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
            "energy_level": self.energy_level
        }


class TrainingRecommendations(db.Model):
    id = db.Column(db.Integer, ForeignKey("trainings.id"))
    user_id = db.Column(db.Integer, ForeignKey("dayview.user_id"))

    def training_recommended(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }