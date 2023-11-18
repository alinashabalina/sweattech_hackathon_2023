from backend.tests.user_service.config import UserService


def test_create_user_successful():
    data = {"username": "test1", "email": "hello2@world.com", "password": "12345"}
    r = UserService().create_a_user(data=data)

    assert r.status_code == 201

    assert r.json()["result"]["username"] == "test1"
    assert r.json()["result"]["email"] == "hello2@world.com"
    assert r.json()["result"]["password"] == "12345"
    assert r.json()["message"] == "User created"
