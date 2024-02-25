import pytest

from main.libraries.di_container import Container


@pytest.fixture
def role_interpreter():
    container = Container()
    return container.role_interpreter()


def test_should_load_settings(role_interpreter):
    role = "admin"
    role_interpreter.load(role)
    assert role_interpreter.get_role() == role


def test_should_prompt_user(role_interpreter):
    role = "admin"
    role_interpreter.load(role)
    msg = "Hi admin, how are you doing today?"
    response = role_interpreter.prompt(msg)
    assert response == f"Response from role {role}"
