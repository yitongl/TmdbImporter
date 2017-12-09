""" Import information from TMDB to a Postgres SQL DB """
import tmdbsimple as tmdb


def get_movie_info(movie_id):
    """ Get information for a specific movie id from TMDB """
    movie = tmdb.Movies(movie_id)
    movie_info = movie.info()
    movie_credits = movie.credits()

    cast = [{'tmdb_id': x['id'], 'name': x['name']} for x in movie_credits['cast']]

    directors = [{'tmdb_id': x['id'], 'name': x['name']}
                 for x in movie_credits['crew'] if x['job'] == 'Director']

    return {
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
