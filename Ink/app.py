from flask import Flask, redirect, render_template, request, session
from Ink import helpers

app = Flask(__name__)

@app.route("/")
@helpers.login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("index.html")