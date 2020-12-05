from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Ink import helpers

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ink.db"
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    hash = db.Column(db.String(500))
    pfpName = db.Column(db.String(400))
    pfp = db.Column(db.LargeBinary)

class profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    skills = db.Column(db.String(1000))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    profession = db.Column(db.String(100))
    experience = db.Column(db.String(20))
    hourlyRate = db.Column(db.Integer)
    totalProjects = db.Column(db.Integer)
    englishLevel = db.Column(db.String(20))
    availabilityNum = db.Column(db.Integer)
    availabilityTime = db.Column(db.String(20))

class jobs(db.Model):
    primaryKey = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    title = db.Column(db.String(500))
    needs = db.Column(db.String(500))
    description = db.Column(db.String(1000))
    deadline = db.Column(db.String(50))
    dayPosted = db.Column(db.String(50))
    email = db.Column(db.String(200))

db.create_all()


def errorhandler(e):
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return helpers.apology(e.name, e.code)


for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
