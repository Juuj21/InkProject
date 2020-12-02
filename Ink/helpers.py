from flask import session, redirect, render_template
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def apology(message, code=400):
    def escape(s):
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


class User():
    def __init__(self, id, username, hash, pfpName, pfp):
        self.id = id
        self.username = username
        self.hash = hash
        self.pfpName = pfpName
        self.pfp = pfp


class Profile():
    def __init__(self, name, description, skills, email, phone, profession, experience, hourlyRate, totalProjects, englishLevel, availabilityNum, availabilityTime):
        self.name = name
        self.description = description
        self.skills = skills
        self.email = email
        self.phone = phone
        self.profession = profession
        self.experience = experience
        self.hourlyRate = hourlyRate
        self.totalProjects = totalProjects
        self.englishLevel = englishLevel
        self.availabilityNum = availabilityNum
        self.availabilityTime = availabilityTime
