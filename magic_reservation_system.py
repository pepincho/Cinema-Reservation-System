# from create_cinema_database import CreateCinemaDatabase


class CommandInterface:

    @staticmethod
    def show_movies(db):
        movies = db.get_all_movies()

        for movie in movies:
            print ("{}. {} - {}".format(movie["movie_id"],
                                        movie["movie_name"],
                                        movie["movie_rating"]))

    @staticmethod
    def show_movie_projections(db, movie_id):
        projections = db.get_all_projections(movie_id)

        # print ("Projection for movie {}".format(projections["movie_name"]))
        # print (projections["movie_name"])
        # print (projections["movie_name"])
        # print ("Projection for movie {}".format(projections[0]))

        for projection in projections:
            print ("Projection for movie {}".format(projection["movie_name"]))
            print ("{} - {} - {} - {}  ".format(projection["projection_id"],
                                                projection["projection_type"],
                                                projection["projection_date"],
                                                projection["projection_time"]))

    # @staticmethod
    # def show_movie_projections(db, movie_id, date):
    #     pass

    @staticmethod
    def make_reservation(db):
        name = input("Enter your name: ")
        counter_tickets = int(input("Chooce number of tickets: "))

        CommandInterface.show_movies(db)

        chosen_movie_id = int(input("Choose a movie: "))
        CommandInterface.show_movie_projections(db, chosen_movie_id)

        chosen_proj_id = int(input("Choose a projection: "))
        hired_seats = db.get_hired_spots(chosen_proj_id)

        available_seats = CommandInterface.get_available_seats(hired_seats)

        print ("Available seats (marked with a dot):")
        for i in available_seats:
            print (" ".join(i))

        counter = 1

        while counter <= counter_tickets:
            str_seats = input("Choose seat {}: ".format(counter))
            str_seats = str_seats.split(",")
            tuple_seats = tuple([int(i) for i in str_seats])

            if tuple_seats in hired_seats:
                print ("This seat is already taken!")
            elif tuple_seats[0] >= 10 or tuple_seats[1] >= 10:
                print ("Lol...NO!")
            else:
                print ("OKAY")
                print (tuple_seats)
                counter += 1


    @staticmethod
    def cancel_reservation():
        pass

    @staticmethod
    def exit():
        pass

    @staticmethod
    def help():
        pass

    @staticmethod
    def get_available_seats(hired_seats):
        rows = 10
        cols = 10
        available_seats = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                           [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        for i in range(0, rows):
            for j in range(0, cols):
                if (i, j) in hired_seats:
                    available_seats[i][j] = "X"
                else:
                    available_seats[i][j] = "."

        return available_seats
