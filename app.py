from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "chickenzarecooll21837"

debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

MOVIES = {"Amadeus", "Chicken Run", "Dances with Wolves"}


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/old-home-page")
def redirect_to_home():
    """Redirects to new home page"""
    flash("That page has moved!")
    return redirect("/")


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/form-2")
def show_form_2():
    return render_template("form_2.html")


COMPLIMENTS = ["cool", "clever", "tenacious", "awesome", "pythonic"]


@app.route("/greeter")
def get_greeting():
    username = request.args["username"]
    compliment = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=compliment)


@app.route("/greeter-2")
def get_greeting_2():
    username = request.args["username"]
    wants_compliments = request.args.get("wants_compliments")
    compliment = choice(COMPLIMENTS)
    nice_things = sample(COMPLIMENTS, 3)
    return render_template(
        "greet_2.html",
        username=username,
        wants_compliments=wants_compliments,
        compliment=nice_things,
    )


@app.route("/lucky")
def lucky_number():
    num = randint(1, 10)
    return render_template("lucky.html", lucky_num=num, msg="you are so lucky!")


@app.route("/spell/<word>")
def spell_word(word):
    caps_word = word.upper()
    return render_template("spell_word.html", word=caps_word)


@app.route("/hello")
def say_hello():
    """Shows Hello Page"""
    return render_template("hello.html")


@app.route("/goodbye")
def say_bye():
    return render_template("goodbye.html")


@app.route("/movies")
def show_all_movies():
    """Show list of all movies in fake DB"""
    return render_template("movies.html", movies=MOVIES)


@app.route("/movies/json")
def get_movies_json():
    return jsonify(list(MOVIES))


@app.route("/movies/new", methods=["POST"])
def add_movie():
    title = request.form["title"]
    # pretend to add to fake DB
    if title in MOVIES:
        flash("Movie Already Exists!", "error")
    else:
        MOVIES.add(title)
        flash("Added your movie!", "success")
    return redirect("/movies")
