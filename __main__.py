""" Main """
import os
from lib.importer import Importer

def main():
    """ Import all movies from TMDB """
    db_username = os.environ['DB_USERNAME']
    db_password = os.environ['DB_PASSWORD']
    db_name = os.environ['DB_NAME']
    api_key = os.environ['TMDB_API_KEY']

    importer = Importer(api_key, db_name, db_username, db_password)
    movie = importer.insert_movie(623)

if __name__ == "__main__":
    main()
