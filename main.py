from create_cinema_database import CreateCinemaDatabase
from add_records_to_cinema_database import AddRecordsToCinemaDatabase
from magic_reservation_system import CommandInterface


def main():
    db = CreateCinemaDatabase()

    AddRecordsToCinemaDatabase.add_movies(db)
    AddRecordsToCinemaDatabase.add_projections(db)
    AddRecordsToCinemaDatabase.add_reservations(db)

    CommandInterface.show_movies(db)
    print (20 * "<>")
    CommandInterface.show_movie_projections(db, 2)
    print (20 * "<>")
    CommandInterface.make_reservation(db)


if __name__ == '__main__':
    main()
