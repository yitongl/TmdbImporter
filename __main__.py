""" Main """
import os
import tmdbsimple as tmdb
import lib.tmdb_importer as importer
from lib.db import DB

def main():
    """ Import all movies from TMDB """
    tmdb.API_KEY = os.environ['TMDB_API_KEY']
    db_username = os.environ['DB_USERNAME']
    db_password = os.environ['DB_PASSWORD']
    db_name = os.environ['DB_NAME']
    db = DB(db_username, db_password, db_name)
    movie = importer.get_movie_info(623)
    db.insert_movie(movie)

    print(movie)

if __name__ == "__main__":
    main()
