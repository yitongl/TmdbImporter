""" Main """
import os
import tmdbsimple as tmdb
import lib.tmdb_importer as importer

def main():
    """ Import all movies from TMDB """
    tmdb.API_KEY = os.environ['TMDB_API_KEY']
    movie = importer.get_movie_info(623)
    print(movie)

if __name__ == "__main__":
    main()
