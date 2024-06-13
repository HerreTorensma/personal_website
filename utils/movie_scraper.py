from imdb import IMDb
import yaml
import re

ia = IMDb()

def search_movie_with_year(query):
    # Extract the title and year from the query using a regular expression
    match = re.match(r"^(.*?)(?:\s*\((\d{4})\))?$", query)
    if not match:
        return None
    
    title = match.group(1).strip()
    year = match.group(2)
    if year:
        year = int(year)
    
    # Search for movies with the given title
    search_results = ia.search_movie(title)
    
    # Filter results by the given year if year is provided
    if year:
        search_results = [movie for movie in search_results if 'year' in movie.data and movie.data['year'] == year]
    
    return search_results

def scrape_movies(filename):
    movie_titles = []

    with open(filename, "r") as file:
        movie_titles = file.readlines()

    custom_movies = []

    for movie_title in movie_titles:
        search_results = search_movie_with_year(movie_title)

        if search_results:
            movie = search_results[0]

            print(f"{movie.get("title")} ({movie.get("year")})")

            custom_movie = {
                "title": movie.get("title"),
                "year": movie.get("year"),
                "cover": movie.get("cover"),
                "url": f"https://www.imdb.com/title/tt{movie.movieID}/"
            }

            custom_movies.append(custom_movie)

    with open("../static/media/movie_info.yaml", "w") as file:
        yaml.dump(custom_movies, file)

if __name__ == "__main__":
    scrape_movies("../static/media/movie_list.txt")