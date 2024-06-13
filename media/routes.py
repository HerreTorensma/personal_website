from flask import Blueprint, render_template
import yaml

media = Blueprint("media", __name__)

@media.get("/")
def media_page():
    # Scrape movies from IMDB
    movies = []
    with open("/static/media/movie_info.yaml", "r") as file:
        movies = yaml.load(file)

    # ia = IMDb()

    # goodfellas = ia.get_movie("0099685")
    # goodfellas.url = f"https://www.imdb.com/title/tt{goodfellas.movieID}/"
    # movies.append(goodfellas)

    return render_template("media.html", movies=movies)