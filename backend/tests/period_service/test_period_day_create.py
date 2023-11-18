from backend.tests.period_service.config import PeriodService


def test_day_create():
    data = {
        "day_id": 3,
        "user_id": 4,
        "day_energy": "weak",
        "period_day_correct": True,
        "training_type": "home"
    }

    r = PeriodService().create_a_day(data=data)

    print(r.json())

