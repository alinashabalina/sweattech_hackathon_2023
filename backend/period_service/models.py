from flask_sqlalchemy import SQLAlchemy

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