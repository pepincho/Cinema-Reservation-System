import sqlite3
import sys
from datetime import datetime, date

# http://www.numericalexpert.com/blog/sqlite_blob_time/sqlite_time_etc.html


class CreateCinemaDatabase:

    def __init__(self):
        # create_movies_table_query = """CREATE TABLE IF NOT EXISTS
        # Movies(
        #     movie_id INTEGER PRIMARY KEY,
        #     movie_name TEXT,
        #     movie_rating INTEGER
        # )"""

        # for now date and time will be text fields
        # create_projections_table_query = """CREATE TABLE IF NOT EXISTS
        # Projections(
        #     projection_id INTEGER PRIMARY KEY,
        #     projection_movie_id INTEGER,
        #     projection_type TEXT,
        #     projection_date TEXT,
        #     projection_time TEXT,
        #     FOREIGN KEY(projection_movie_id) REFERENCES Movies(movie_id)
        # )"""

        # create_reservations_table_query = """CREATE TABLE IF NOT EXISTS
        # Reservations(
        #     reservation_id INTEGER PRIMARY KEY,
        #     reservation_username TEXT,
        #     reservation_projection_id INTEGER,
        #     reservation_row INTEGER,
        #     reservation_col INTEGER
        #     FOREIGN KEY(reservation_projection_id)
        #     REFERENCES Projections(projection_id)
        # )"""

        self.database = sqlite3.connect("cinema_database")
        self.database.row_factory = sqlite3.Row
        self.cursor = self.database.cursor()

        self.cursor.execute(create_movies_table_query)
        self.cursor.execute(create_projections_table_query)
        self.cursor.execute(create_reservations_table_query)

    def add_movie(self, name, rating):
        self.cursor.execute("""INSERT INTO Movies(
            movie_name,
            movie_rating)
            VALUES(?,?)""", (name, rating))

    def add_projection(self, movie_id, proj_type, data, time):
        self.cursor.execute("""INSERT INTO Projections(
            projection_movie_id,
            projection_type,
            projection_date,
            projection_time)
            VALUES(?,?,?,?)""", (movie_id, proj_type, data, time))

    def add_reservation(self, username, proj_id, row, col):
        self.cursor.execute("""INSERT INTO Projections(
            reservation_username,
            reservation_projection_id,
            reservation_row,
            reservation_col)
            VALUES(?,?,?,?)""", (username, proj_id, row, col))

    def get_all_movies(self):
        pass
