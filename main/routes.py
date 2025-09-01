from flask import Blueprint, render_template, redirect, url_for, request, session
import os
from blog import utils

main = Blueprint("main", __name__)

@main.route("/")
def home():
    articles = utils.get_all_articles_metadata("articles")[:3]
    return render_template("home.html", articles=articles)

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/secret")
def secret():
    if "yes" in session:
        return render_template("secret.html")
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") == "fuckyou":
            session["yes"] = "yes"
            return redirect(url_for("main.secret"))
        else:
            return render_template("login.html", error="Wrong password.")

    return render_template("login.html")