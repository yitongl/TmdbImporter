""" Database module """
import psycopg2

class DB(object):
    """ Database connector """
    def __init__(self, username, password, database):
        # Connect to an existing database
        self.conn = psycopg2.connect(database=database, user=username, password=password)

    def __get_or_create_genres(self, cur, genres):
        ids  = []
        for genre in genres:
            cur.execute("SELECT id FROM genres WHERE name = %s;", (genre, ))
            id = cur.fetchone()
            if not id:
                cur.execute("INSERT into genres (name) VALUES (%s);", (genre, ))
                self.conn.commit()
                cur.execute("SELECT id FROM genres WHERE name = %s;", (genre, ))
                id = cur.fetchone()

            ids.append(id[0])

        return ids

    def __get_or_create_persons(self, cur, persons):
        # TODO: Similar as genres
        pass

    def insert_movie(self, movie):
        cur = self.conn.cursor()

        genres = self.__get_or_create_genres(cur, movie['genres'])
        cast = self.__get_or_create_persons(cur, movie['cast'])
        directors = self.__get_or_create_persons(cur, movie['directors'])
        # TODO: Insert movie and create relations to genres and persons


        cur.close()

    def close(self):
        self.conn.close()
