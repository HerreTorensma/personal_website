from flask import Blueprint, render_template
import os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/gallery")
def gallery():
    pictures = os.listdir("static/gallery")
    paths = []
    for picture in pictures:
        paths.append(os.path.join("/static/gallery", picture))

    return render_template("gallery.html", pictures=paths)

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/about")
def about():
    return render_template("about.html")