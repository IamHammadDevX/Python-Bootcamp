from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route("/")
def name():
    rand_num = random.randint(1, 10)
    curr_year = datetime.datetime.now().year
    return render_template("index.html", num=rand_num, year=curr_year)

@app.route("/guess/<name>")
def age(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)