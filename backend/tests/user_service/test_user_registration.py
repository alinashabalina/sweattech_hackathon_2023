from copy import deepcopy
from backend.tests.user_service.config import UserService

def test_create_user_successful():
    data = {"username": "test1", "email": "hello2@world.com", "password": "12345"}
    r = UserService().create_a_user(data=data)

    assert r.status_code == 201

    assert r.json()["result"]["username"] == "test1"
    assert r.json()["result"]["email"] == "hello2@world.com"
    assert r.json()["result"]["password"] == "12345"
    assert r.json()["message"] == "User created"

def test_create_user_unsuccessful_username_missing():
    data = {"email": "hello@world.com", "password": "12345"}
    r = UserService().create_a_user(data=data)

    assert r.status_code == 201
    assert r.json()["result"]["username"] == ""
    assert r.json()["result"]["email"] == "hello@world.com"
    assert r.json()["result"]["password"] == "12345"
    assert r.json()["message"] == "User created"

def _checks_400(r):
    assert r.status_code == 400
    assert "Validation error" in r.json()["message"]

def test_create_user_unsuccessful_email_missing():
    data = {"username": "test", "password": "12345"}
    result = UserService().create_a_user(data=data)

    _checks_400(result)

def test_create_user_unsuccessful_password_missing():
    data = {"username": "test", "email": "hello@world.com"}
    result = UserService().create_a_user(data=data)

    assert result.status_code == 400
    assert result.json()["message"] == 'Make sure you have filled the password field'

def test_create_user_unsuccessful_extra_field():
    data = {"username": "test", "email": "hello@world.com", "password": "12345"}
    data["message"] = "opop"
    r = UserService().create_a_user(data=data)

    _checks_400(r)


def test_create_user_unsuccessful_empty_body():
    r = UserService().create_a_user(data={})

    _checks_400(r)


def test_create_user_unsuccessful_wrong_data_type():
    data = {"username": 1, "email": "hello@world.com", "password": "12345"}
    r1 = UserService().create_a_user(data=data)

    data = {"username": "test", "email": "hello@world.com", "password": 12345}
    r2 = UserService().create_a_user(data=data)

    data = {"username": "test", "email": True, "password": "12345"}
    r3 = UserService().create_a_user(data=data)

    for r in [r1, r2, r3]:
        _checks_400(r)