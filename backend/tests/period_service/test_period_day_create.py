from backend.tests.period_service.config import PeriodService


def test_day_create():
    data = {
        "date": "28101991",
        "user_id": 1,
        "day_energy": "strong",
        "period_day_correct": False,
        "training_type": "home"
    }

    r = PeriodService().create_a_day(data=data)

    print(r.json())

