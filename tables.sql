DROP TABLE IF EXISTS Movies;

CREATE TABLE IF NOT EXISTS Movies(
    movie_id INTEGER PRIMARY KEY,
    movie_name TEXT,
    movie_rating INTEGER
);

DROP TABLE IF EXISTS Projections;

CREATE TABLE IF NOT EXISTS Projections(
    projection_id INTEGER PRIMARY KEY,
    projection_movie_id INTEGER,
    projection_type TEXT,
    projection_date TEXT,
    projection_time TEXT,
    FOREIGN KEY(projection_movie_id) REFERENCES Movies(movie_id)
);

DROP TABLE IF EXISTS Reservations;

CREATE TABLE IF NOT EXISTS Reservations(
    reservation_id INTEGER PRIMARY KEY,
    reservation_username TEXT,
    reservation_projection_id INTEGER,
    reservation_row INTEGER,
    reservation_col INTEGER,
    FOREIGN KEY(reservation_projection_id) REFERENCES Projections(projection_id)
);
