from create_cinema_database import CreateCinemaDatabase


class AddRecordsToCinemaDatabase:

    @staticmethod
    def add_movies(db):
        db.add_movie("The Hunger Games: Catching Fire", 7.9)
        db.add_movie("Wreck-It Ralph", 7.8)
        db.add_movie("Her", 8.3)
        db.add_movie("Spiderman", 9)

    @staticmethod
    def add_projections(db):
        db.add_projection(1, "3D", "2014-04-01", "19:10")
        db.add_projection(1, "2D", "2014-04-01", "19:00")
        db.add_projection(1, "4DX", "2014-04-02", "21:00")
        db.add_projection(3, "2D", "2014-04-05", "20:20")
        db.add_projection(2, "3D", "2014-04-02", "22:00")
        db.add_projection(2, "2D", "2014-04-02", "19:30")
        db.add_projection(4, "4DX", "2014-09-19", "19:30")
        db.add_projection(4, "3D", "2014-05-14", "19:30")
        db.add_projection(4, "3D", "2014-05-14", "22:30")
        db.add_projection(4, "5D", "2015-05-14", "19:30")



    @staticmethod
    def add_reservations(db):
        db.add_reservation("RadoRado", 1, 2, 1)
        db.add_reservation("RadoRado", 1, 3, 5)
        db.add_reservation("RadoRado", 1, 7, 8)
        db.add_reservation("Ivo", 3, 1, 1)
        db.add_reservation("Ivo", 3, 1, 2)
        db.add_reservation("Pesho", 5, 2, 3)
        db.add_reservation("Pesho", 5, 2, 4)
