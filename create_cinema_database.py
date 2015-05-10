import sqlite3
import sys
from datetime import datetime, date
from settings import DB_NAME, SQL_FILE

# http://www.numericalexpert.com/blog/sqlite_blob_time/sqlite_time_etc.html


class CreateCinemaDatabase:

    ROW_SIZE = 10
    COL_SIZE = 10

    def __init__(self):
        self.database = sqlite3.connect(DB_NAME)
        self.database.row_factory = sqlite3.Row
        self.cursor = self.database.cursor()

        with open(SQL_FILE, "r") as f:
            self.database.executescript(f.read())
            self.database.commit()

    def add_movie(self, name, rating):
        self.cursor.execute("""INSERT INTO Movies(
            movie_name,
            movie_rating)
            VALUES(?,?)""", (name, rating))
        self.database.commit()

    def add_projection(self, movie_id, proj_type, data, time):
        self.cursor.execute("""INSERT INTO Projections(
            projection_movie_id,
            projection_type,
            projection_date,
            projection_time)
            VALUES(?,?,?,?)""", (movie_id, proj_type, data, time))
        self.database.commit()

    def add_reservation(self, username, proj_id, row, col):
        self.cursor.execute("""INSERT INTO Reservations(
            reservation_username,
            reservation_projection_id,
            reservation_row,
            reservation_col)
            VALUES(?,?,?,?)""", (username, proj_id, row, col))
        # self.database.commit()

    def get_all_movies(self):
        return self.cursor.execute("""SELECT movie_id, movie_name, movie_rating
            FROM Movies
            ORDER BY movie_rating ASC""")

    def get_all_projections(self, movie_id):
        return self.cursor.execute(
            """SELECT P.projection_id,
                        P.projection_type,
                        P.projection_date,
                        P.projection_time,
                        M.movie_name
            FROM Projections AS P
            INNER JOIN Movies AS M
            ON P.projection_movie_id = M.movie_id
            WHERE M.movie_id = ?""", (movie_id,))

    def get_all_projections_date(self, movie_id, datee):
        return self.cursor.execute(
            """SELECT P.projection_id,
                        P.projection_type,
                        P.projection_date,
                        P.projection_time,
                        M.movie_name
            FROM Projections AS P
            INNER JOIN Movies AS M
            ON P.projection_movie_id = M.movie_id
            WHERE M.movie_id = ?
            AND P.projection_date = ?""", (movie_id, datee))

    def get_hired_spots(self, proj_id):
        hired_seats = []
        info = self.cursor.execute("""SELECT R.reservation_row, R.reservation_col
            FROM Reservations AS R
            INNER JOIN Projections AS P
            ON R.reservation_projection_id = P.projection_id
            WHERE P.projection_id = ?""", (proj_id,))

        for i in info:
            seat = (int(i["reservation_row"]), int(i["reservation_col"]))
            hired_seats.append(seat)

        return hired_seats

    def get_movie(self, movie_id):
        # try:
        name = self.cursor.execute("""SELECT movie_name FROM Movies
            WHERE movie_id = ?""", (movie_id,))
        return name.fetchone()[0]
        # except:
        #     return -1

    def delete_reservation(self, username, proj_id):
        self.cursor.execute("""DELETE FROM Reservations
            WHERE reservation_username = ?
            AND reservation_projection_id = ?""", (username, proj_id))
        self.database.commit()

    def get_date_time_projection(self, proj_id):
        proj_date_time = self.cursor.execute("""SELECT projection_date, projection_time
                                    FROM Projections
                                    WHERE projection_id = ?""", (proj_id,))
        return proj_date_time.fetchone()

    def get_projection(self, proj_id):
        projection = self.cursor.execute("""SELECT * FROM Projections
                                WHERE projection_id = ?""", (proj_id,))
        return projection.fetchone()
