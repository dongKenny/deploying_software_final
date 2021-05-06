import pytest
import requests

from pytest_bdd import scenarios, given, when, then

CLASS_API = "https://www.dnd5eapi.co/api/classes/"
scenarios("../features/api.feature", example_converters=dict(dnd_class=str, hit_die=int, saving_throws=str))


@pytest.fixture
@when("The DnD API is queried with Wizard")
def class_response_fail():
    params = {"format": "json"}
    response = requests.get(CLASS_API + "Wizard", params=params)
    return response


@then("The Response code is not 200")
def class_response_code_fail(class_response_fail):
    assert class_response_fail.status_code != 200


@pytest.fixture
@when('The DnD API is queried with "<dnd_class>"')
def class_response(dnd_class):
    params = {"format": "json"}
    response = requests.get(CLASS_API + dnd_class, params=params)
    return response


@then("The response code is 200")
def class_response_code(class_response):
    assert class_response.status_code == 200


@then('The hit_die is "<hit_die>"')
def class_hit_die(class_response, hit_die):
    assert class_response.json()["hit_die"] == int(hit_die)


@then('The saving throws are "<saving_throws>"')
def class_saving_throw(class_response, saving_throws):
    firstThrow = class_response.json()["saving_throws"][0]["index"]
    secondThrow = class_response.json()["saving_throws"][1]["index"]
    assert firstThrow + ", " + secondThrow == saving_throws
