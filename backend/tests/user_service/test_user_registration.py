from backend.tests.user_service.config import UserService


def test_create_user_successful():
    data = {"username": "test7", "email": "hello5@world.com", "password": "12346"}
    r = UserService().create_a_user(data=data)
    print(r.json())

    assert r.status_code == 201

