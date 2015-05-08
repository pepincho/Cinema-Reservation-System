from create_cinema_database import CreateCinemaDatabase


class AddRecordsToCinemaDatabase:

    @staticmethod
    def add_movies(db):
        db.add_movie("The Hunger Games: Catching Fire", 7.9)
        db.add_movie("Wreck-It Ralph", 7.8)
        db.add_movie("Her", 8.3)

    @staticmethod
    def add_projections(db):
        db.add_projection(1, "3D", "", "")
        db.add_projection(1, "2D", "", "")
        db.add_projection(1, "4DX", "", "")
        db.add_projection(3, "2D", "", "")
        db.add_projection(2, "3D", "", "")
        db.add_projection(2, "2D", "", "")

    @staticmethod
    def add_reservations(db):
        db.add_reservation("RadoRado", 1, 2, 1)
        db.add_reservation("RadoRado", 1, 3, 5)
        db.add_reservation("RadoRado", 1, 7, 8)
        db.add_reservation("Ivo", 3, 1, 1)
        db.add_reservation("Ivo", 3, 1, 2)
        db.add_reservation("Pesho", 5, 2, 3)
        db.add_reservation("Pesho", 5, 2, 4)
