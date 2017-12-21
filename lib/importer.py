""" Import information from TMDB to a Postgres SQL DB """
import tmdbsimple as tmdb
from lib.db import DB

class Importer(object):
    def __init__(self, tmdb_api_key, db_name, db_username, db_password):
        tmdb.API_KEY = tmdb_api_key
        self.database = DB(db_username, db_password, db_name)

    def insert_movie(self, movie_id):
        """ Get information for a specific movie id from TMDB """
        movie = tmdb.Movies(movie_id)
        movie_info = movie.info()
        movie_credits = movie.credits()

        cast = [{'tmdb_id': x['id'], 'name': x['name']} for x in movie_credits['cast']]

        directors = [{'tmdb_id': x['id'], 'name': x['name']}
                     for x in movie_credits['crew'] if x['job'] == 'Director']

        movie = {
            'tmdb_id': movie_info['id'],
            'imdb_id': movie_info['imdb_id'],
            'title': movie_info['title'],
            'rating': movie_info['vote_average'],
            'votes': movie_info['vote_count'],
            'revenue': movie_info['revenue'],
            'budget': movie_info['budget'],
            'popularity': movie_info['popularity'],
            'runtime': movie_info['runtime'],
            'tagline': movie_info['tagline'],
            'release_date': movie_info['release_date'],
            'genres': [x['name'] for x in movie_info['genres']],
            'cast': cast,
            'directors': directors,
        }

        self.database.insert_movie(movie)
