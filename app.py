from flask import Flask, render_template, request, flash, session
import os

from helpers.validation import valid_password
import helpers.users
import helpers.data_handling

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create-account", methods=["GET", "POST"])
def create_account():
    if request.method == "GET":
        return render_template("create_account.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if not valid_password(password):
            session.pop("_flashes", None)
            flash("Insecure password")
            return render_template("create_account.html")

        helpers.users.new_user(username, password)
        users = helpers.data_handling.get("users")
        return render_template("profile.html", user=users[username])

@app.route("/log-in", methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template("login.html")
    else:
        users = helpers.data_handling.get("users")
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username not in users.keys():
            flash("Invalid Username")
            pass
        elif users[username]["password"] != password:
            flash("Incorrect password")
            pass
        
        globals = helpers.data_handling.get("globals")
        globals["logged_in"] = username
        globals.data_handling.update("globals", globals)
        return render_template("profile.html", user=users[username])


@app.route("/@<username>/")
def profile(username):
    globals = helpers.data_handling.get("globals")
    users = helpers.data_handling.get("users")
    if globals["logged_in"]:
        return render_template("profile.html", user=users[username])
    else:
        return render_template("index.html")


app.run("0.0.0.0")
