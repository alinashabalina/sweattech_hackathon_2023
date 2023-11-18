from backend.tests.period_service.config import PeriodService


def test_recommendations():
    r = PeriodService().get_a_recommendation(user_id=1, date="28101991")
    assert r.status_code == 200