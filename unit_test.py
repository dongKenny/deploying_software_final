import app
import pytest
import requests

CLASS_API = "https://www.dnd5eapi.co/api/classes/"


@pytest.fixture()
def test_generate_response_failure():
    params = {"format": "json"}
    response = requests.get(CLASS_API + "Wizard", params=params)
    return response


def test_get_status_code_failure(test_generate_response_failure):
    assert test_generate_response_failure.status_code != 200


@pytest.fixture()
def test_generate_response_success():
    params = {"format": "json"}
    response = requests.get(CLASS_API + "wizard", params=params)
    return response


def test_get_status_code_success(test_generate_response_success):
    assert test_generate_response_success.status_code == 200


def test_get_hit_die(test_generate_response_success):
    assert test_generate_response_success.json()["hit_die"] == 6


def test_get_saving_throw(test_generate_response_success):
    firstThrow = test_generate_response_success.json()["saving_throws"][0]["index"]
    secondThrow = test_generate_response_success.json()["saving_throws"][1]["index"]
    assert firstThrow + ", " + secondThrow == "int, wis"
