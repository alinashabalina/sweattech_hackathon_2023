from backend.tests.user_service.config import UserService


def test_user_question():
    data = {
        "user_id": 1,
        "username": "Tina",
        "date_of_birth": "28.12.1995",
        "hormone_state": "menstruation",
        "day_of_cycle": 3,
        "goal_list": "strength"
    }

    r = UserService().question_a_user(data=data)
    assert r.status_code == 201