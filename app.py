from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    result = db.session.execute("SELECT COUNT(*) FROM users")
    count = result.fetchone()[0]
    return render_template("index.html")

@app.route("/kirjautuminen")
def kirjautuminen():
    return render_template("kirjautuminen.html")

@app.route("/uusi_tunnus")
def uusi_tunnus():
    return render_template("uusi_tunnus.html")

@app.route("/turhat")
def turhat():
    return "Tähän pian tulossa turhaa turinaa"

@app.route("/loysat")
def loysat():
    return "Tähän pian tulossa löysää löpinää"

