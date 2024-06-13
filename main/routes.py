from flask import Blueprint, render_template
import os
from blog import utils

main = Blueprint("main", __name__)

@main.route("/")
def home():
    articles = utils.get_all_articles_metadata("articles")[:3]
    return render_template("home.html", articles=articles)

@main.route("/gallery")
def gallery():
    pictures_path = os.listdir("static/gallery/images")
    pictures = []

    metadata = []
    for picture in pictures_path:
        picture_path = os.path.join("/static/gallery/images", picture)
        pictures.append(picture_path)

        if os.path.exists(picture_path):
            print("picture path exists")

        # metadata_path = os.path.join("/static/gallery/metadata", f"{os.path.splitext(picture)[0]}.yml")
        metadata_path = f"/static/gallery/metadata/{os.path.splitext(picture)[0]}.yml"
        print(metadata_path)
        if os.path.exists(metadata_path):
            print()
            print("there is metadata for " + metadata_path)
            print()

    return render_template("gallery.html", pictures=pictures)

@main.route("/projects")
def projects():
    return render_template("projects.html")

@main.route("/about")
def about():
    return render_template("about.html")