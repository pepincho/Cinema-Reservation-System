from create_cinema_database import CreateCinemaDatabase
from add_records_to_cinema_database import AddRecordsToCinemaDatabase
from magic_reservation_system import CommandInterface


def main():
    db = CreateCinemaDatabase()

    interface = CommandInterface(db)

    AddRecordsToCinemaDatabase.add_movies(db)
    AddRecordsToCinemaDatabase.add_projections(db)
    AddRecordsToCinemaDatabase.add_reservations(db)

    print (30 * "<>")

    interface.start()


if __name__ == '__main__':
    main()
