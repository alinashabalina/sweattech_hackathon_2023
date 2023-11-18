from backend.tests.period_service.config import PeriodService


def test_create_a_training():
    data = {
        "name": "qwertz",
        "energy_level": "strong",
        "link": "https://www.youtube.com/shorts/Anu1AoD-9NY"
    }
    r = PeriodService().create_a_training(data=data)
    assert r.status_code == 201