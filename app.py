from flask import Flask, request, render_template
import requests

CLASS_API = "https://www.dnd5eapi.co/api/classes/"
app = Flask(__name__, template_folder="templates")


def generate_response(dnd_class):
    params = {"format": "json"}
    return requests.get(CLASS_API + dnd_class, params=params)


def get_status_code(class_response):
    return class_response.status_code


def get_hit_die(class_response):
    return class_response.json()["hit_die"]


def get_saving_throw(class_response):
    return class_response.json()["saving_throws"]


def dnd_api_call(dnd_class):
    classes = {"barbarian", "bard", "cleric", "druid", "fighter", "monk", "paladin", "ranger", "rogue", "sorcerer",
               "warlock", "wizard"}

    result = "API call made to: " + CLASS_API + dnd_class + "\n"

    response = generate_response(dnd_class)

    result += "Response for api call was: %d\n" % get_status_code(response)

    if dnd_class not in classes:
        return result

    result += "Hit die is: %s\n" % get_hit_die(response)

    throws = get_saving_throw(response)
    firstThrow = throws[0]["index"]
    secondThrow = throws[1]["index"]

    result += "Saving throws are: " + firstThrow + ", " + secondThrow
    return result


@app.route('/dnd', methods=['GET', 'POST'])
def dnd():
    result = ""
    if request.method == "POST":
        class_name = request.form.get("class")

        if class_name is not None:
            result = "Your api result using %s:\n" % class_name
            result += dnd_api_call(dnd_class=class_name)

    return render_template("dnd.html", message=result.split("\n"))


@app.route('/')
def index():
    return 'Go to /dnd instead!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')