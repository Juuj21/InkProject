from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, session
from sqlite3 import connect

from Ink.__init__ import *
from Ink.helpers import *
from Ink.config import *

@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user_id = session["user_id"]

    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        skills = request.form.get("skills")
        email = request.form.get("email")
        phone = request.form.get("phone")
        profession = request.form.get("profession")
        experience = request.form.get("experience")
        hourlyRate = request.form.get("hourlyRate")
        totalProjects = request.form.get("totalProjects")
        englishLevel = request.form.get("englishLevel")
        availabilityNum = request.form.get("availabilityNum")
        availabilityTime = request.form.get("availabilityTime")

        info = {'name':name, 'description':description, 'skills':skills, 'email':email, 'phone':phone, 'profession':profession, 'experience':experience, 'hourlyRate':hourlyRate, 'totalProjects':totalProjects, 'englishLevel':englishLevel, 'availabilityNum':availabilityNum, 'availabilityTime':availabilityTime}

        if skills != "" and skills != None:
            skills = skills.split(",")
            if len(skills) > 6:
                return apology("Can only contain 6 skills", 403)

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT id FROM profiles")
            cursor.close()

        for key, data in info.items():
            if data == "":
                with connect("Ink.db") as con:
                    cursor = con.cursor()
                    cursor.execute(f"SELECT {key} FROM profiles WHERE id = {user_id}")

                    dbData = cursor.fetchall()
                    cursor.close()

                if dbData[0][0] == None:
                    return apology(f"You have to type the {key}", 400)
                else:
                    data = dbData

            else:
                with connect("ink.db") as con:
                    cursor = con.cursor()
                    cursor.execute(f"""UPDATE profiles SET {key} = '{data.replace("'", "´")}' WHERE id = {user_id}""")

                    con.commit()
                    cursor.close()

        for key, data in info.items():
            with connect("ink.db") as con:
                cursor = con.cursor()
                cursor.execute(f"SELECT {key} FROM profiles WHERE id = {user_id}")
                info[f'{key}'] = cursor.fetchall()
                cursor.close()

        infoValues = []

        for values in info.values():
            infoValues.append(values[0][0])

        infoValues[2] = infoValues[2].split(',')

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT pfp FROM users WHERE id = {user_id}")
            pfp = cursor.fetchall()
            cursor.close()

        if "x" not in str(pfp[0][0]):
            pfp = "static/pfp/pfpDefault.png"
        else:
            pfp = f"static/pfp/pfp{user_id}.jpg"

        return render_template("profile.html", name=infoValues[0], description=infoValues[1], skills=infoValues[2], email=infoValues[3], phone=infoValues[4], profession=infoValues[5], experience=infoValues[6], hourlyRate=infoValues[7], totalProjects=infoValues[8], englishLevel=infoValues[9], availabilityNum=infoValues[10], availabilityTime=infoValues[11], profilepic=pfp)

    else:
        infoNames = {'name':"", 'description':"", 'skills':"", 'email':"", 'phone':"", 'profession':"", 'experience':"", 'hourlyRate':0, 'totalProjects':0, 'englishLevel':"", 'availabilityNum':0, 'availabilityTime':""}

        values = []

        for key in infoNames.keys():
            with connect("ink.db") as connec:
                cursor = connec.cursor()
                cursor.execute(f"SELECT {key} FROM profiles WHERE id = {user_id}")

                infoNames[f'{key}'] = cursor.fetchall()
                cursor.close()

        for value in infoNames.values():
            values.append(value[0][0])

        try:
            values[2] = values[2].split(",")
        except:
            try:
                values[2][0] = values[2].split(",")
            except:
                try:
                    values[2][0] = values[2][0]
                except:
                    values[2] = values[2]

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT pfp FROM users WHERE id = {user_id}")
            pfpCheck = cursor.fetchall()[0][0]
            cursor.close()

        fileData = users.query.filter_by(id=user_id).first()

        if fileData.pfp != None and len(fileData.pfp) > 0:

            with open(f"static/pfp/pfp{user_id}.jpg", "wb") as file:
                file.write(fileData.pfp)

            profilepic = f"static/pfp/pfp{user_id}.jpg"

        else:

            if "x" in str(pfpCheck):
                profilepic = f"static/pfp/pfp{user_id}.jpg"
            else:
                profilepic = "static/pfp/pfpDefault.png"

        if values[2] == None:
            values[2] = ["None"]

        return render_template("profile.html", name=values[0], description=values[1], skills=values[2], email=values[3], phone=values[4], profession=values[5], experience=values[6], hourlyRate=values[7], totalProjects=values[8], englishLevel=values[9], availabilityNum=values[10], availabilityTime=values[11], profilepic=profilepic)


@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    user_id = session["user_id"]

    if request.method == "POST":
        pfp = "static/pfp/pfpDefault.png"
        file = request.files['inputFile']

        fileName = f"pfp{user_id}.jpg"
        fileData = file.read()

        if "x" in str(fileData):
            user = users.query.filter_by(id=user_id).first()
            user.pfpName = fileName
            user.pfp = fileData
            db.session.commit()

        else:
            with connect("ink.db") as con:
                cursor = con.cursor()
                cursor.execute(f"SELECT pfp FROM users WHERE id = {user_id}")
                pfp = cursor.fetchall()[0][0]
                cursor.close()

            if "x" in str(pfp):
                pfp = f"static/pfp/pfp{user_id}.jpg"
            else:
                pfp = "static/pfp/pfpDefault.png"

        return redirect("/profile")

    else:
        return render_template("upload.html")


@app.route("/editprofile", methods=["GET", "POST"])
@login_required
def editprofile():
    if request.method == "POST":
        return render_template("profile.html")
    else:
        return render_template("editprofile.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide password", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif not request.form.get("username").isalnum():
            return apology("username can contain only letters and numbers", 403)
        
        username = request.form.get("username").lower()
        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT username FROM users")
            dbUsernames = cursor.fetchall()

            matchs = 0

            for name in dbUsernames:
                if username in name:
                    matchs += 1

            if matchs != 1:
                return apology("Username not found", 403)

            cursor.execute("SELECT hash FROM users WHERE username = ?", (username,))
            dbHash = cursor.fetchone()
            cursor.close()

        if not check_password_hash(dbHash[0], request.form.get("password")):
            return apology("Invalid username and/or password", 403)

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            user_id = cursor.fetchone()
        
        session["user_id"] = user_id[0]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 403)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and password confirmation must match", 403)

        username = request.form.get("username").lower()
        password = generate_password_hash(request.form.get("password"))

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute("SELECT username FROM users")
            names = cursor.fetchall()

            for rows in names:
                for dbUsername in rows:
                    if username == dbUsername:
                        return apology("That username already exists", 400)

            newUser = users(username=username, hash=password, pfpName=None, pfp=None)

            db.session.add(newUser)
            db.session.commit()
            
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            user_id = cursor.fetchone()

            cursor.execute("INSERT INTO profiles (id) VALUES (?)", (user_id))
            con.commit()

            cursor.close()

        return redirect("/")

    else:
        return render_template("register.html")
        

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        if request.form.get("radio") == "yes":
            user_id = session["user_id"]

            with connect("ink.db") as con:
                cursor = con.cursor()
                cursor.execute(f"DELETE FROM profiles WHERE id = {user_id}")
                cursor.close()
            
            user = users.query.filter_by(id=user_id).first()

            db.session.delete(user)
            db.session.commit()
            session.clear()

            return redirect("/")
        else:
            return redirect("/profile")
    else:
        return render_template("delete.html")


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        user_id = session["user_id"]

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT hash FROM users WHERE id = {user_id}")
            dbHash = cursor.fetchall()
            cursor.close()

        if not request.form.get("currentPassword"):
            return apology("You have to type your password", 403)
        
        elif not request.form.get("newPassword"):
            return apology("You have to type your new password", 403)

        elif not request.form.get("confirmNewPassword"):
            return apology("You have to type your new password confirmation", 403)

        currentPassword = request.form.get("currentPassword")
        newPassword = request.form.get("newPassword")
        confirmNewPassword = request.form.get("confirmNewPassword")

        if not check_password_hash(dbHash[0][0], currentPassword):
            return apology("Wrong password", 403)
        
        elif newPassword != confirmNewPassword:
            return apology("New password and its confirmation must match", 403)

        user = users.query.filter_by(id=user_id).first()

        user.hash = generate_password_hash(newPassword)
        db.session.commit()
        
        return redirect("/profile")
    else:
        return render_template("password.html")


@app.route("/change-username", methods=["GET", "POST"])
@login_required
def change_username():
    if request.method == "POST":
        user_id = session["user_id"]

        with connect("ink.db") as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT hash FROM users WHERE id = {user_id}")
            dbHash = cursor.fetchall()
            cursor.close()

        if not request.form.get("newUsername"):
            return apology("Must contain your new username", 403)
        
        elif not request.form.get("password"):
            return apology("Must contain your password", 403)

        newUsername = request.form.get("newUsername")
        password = request.form.get("password")

        if not check_password_hash(dbHash[0][0], password):
            return apology("Wrong password", 403)

        user = users.query.filter_by(id=user_id).first()

        user.username = newUsername
        db.session.commit()

        return redirect("/profile")
    else:
        return render_template("username.html")
