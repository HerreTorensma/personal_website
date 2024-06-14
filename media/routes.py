from flask import Blueprint, render_template
import yaml

media = Blueprint("media", __name__)

@media.route("/")
def media_page():
    movies = []

    with open("static/media/movie_info.yml", "r") as file:
        movies = yaml.safe_load(file)

    return render_template("media.html", movies=movies)