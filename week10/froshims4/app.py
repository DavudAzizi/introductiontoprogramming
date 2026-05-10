from flask import Flask, redirect, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

registrants = {}


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")

    if not name:
        return render_template("error.html", message="Missing name")

    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    registrants[name] = sport
    return redirect("/registrants")


@app.route("/registrants")
def show_registrants():
    return render_template("registrants.html", registrants=registrants)
