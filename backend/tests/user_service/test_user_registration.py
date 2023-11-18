from copy import deepcopy
from backend.tests.user_service.config import UserService

def test_create_user_successful(create_user):
    assert create_user[0].json()["result"]["email"] == create_user[1]["email"]
    assert create_user[0].json()["result"]["username"] == create_user[1]["username"]

def _checks_400(r):
    assert r.status_code == 400
    assert "Validation error" in r.json()["message"]

def test_create_user_unsuccessful_required_field_missing(create_user_body):
    data = deepcopy(create_user_body)
    data.pop("email")
    result = UserService().create_a_user(data=data)

    _checks_400(result)

def test_create_user_unsuccessful_not_required_field_missing(create_user_body):
    data = deepcopy(create_user_body)
    data.pop("username")
    r = UserService().create_a_user(data=data)

    assert r.status_code == 201
    assert r.json()["message"] == SuccessfulResponses.created["message"]
    assert r.json()["result"]["username"] == ""


def test_create_user_unsuccessful_extra_field(create_user_body):
    data = deepcopy(create_user_body)
    data["message"] = "opop"
    r = UserService().create_a_user(data=data)

    _checks_400(r)


def test_create_user_unsuccessful_empty_body():
    r = UserService().create_a_user(data={})

    _checks_400(r)


def test_create_user_unsuccessful_wrong_data_type(create_user_body):
    data = deepcopy(create_user_body)
    data["username"] = 1
    r1 = UserService().create_a_user(data=data)

    data = deepcopy(create_user_body)
    data["is_admin"] = "opop"
    r2 = UserService().create_a_user(data=data)

    data = deepcopy(create_user_body)
    data["email"] = True
    r3 = UserService().create_a_user(data=data)

    for r in [r1, r2, r3]:
        _checks_400(r)