from backend.tests.period_service.config import PeriodService


def test_get_user_day():
    r = PeriodService().get_a_day(user_id=4, day_id=3)
    print(r.json())