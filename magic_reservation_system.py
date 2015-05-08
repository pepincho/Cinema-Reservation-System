# from create_cinema_database import CreateCinemaDatabase
import sys


class CommandInterface:

    def __init__(self, db):
        self.__cinema = db

    def show_movies(self):
        movies = self.__cinema.get_all_movies()

        for movie in movies:
            print ("{}. {} - {}".format(movie["movie_id"],
                                        movie["movie_name"],
                                        movie["movie_rating"]))

    def show_movie_projections(self, movie_id):

        movie_name = self.__cinema.get_movie(movie_id)
        print ("Projection for movie {}".format(movie_name))

        projections = self.__cinema.get_all_projections(movie_id)

        for projection in projections:
            print ("{} - {} - {} - {}  ".format(projection["projection_id"],
                                                projection["projection_type"],
                                                projection["projection_date"],
                                                projection["projection_time"]))

    # @staticmethod
    # def show_movie_projections(db, movie_id, date):
    #     pass

    def make_reservation(self):
        self.username = input("Enter your name: ")
        self.counter_tickets = int(input("Chooce number of tickets: "))

        self.show_movies()

        self.chosen_movie_id = int(input("Choose a movie: "))
        self.show_movie_projections(self.chosen_movie_id)

        self.chosen_proj_id = int(input("Choose a projection: "))
        self.hired_seats = self.__cinema.get_hired_spots(self.chosen_proj_id)

        available_seats = CommandInterface.get_available_seats(
            self.hired_seats)

        print ("Available seats (marked with a dot):")
        for i in available_seats:
            print (" ".join(i))

        counter = 1

        self.chosen_seats = []

        while counter <= self.counter_tickets:
            str_seats = input("Choose seat {}: ".format(counter))
            str_seats = str_seats.split(",")
            tuple_seats = tuple([int(i) for i in str_seats])

            if tuple_seats in self.hired_seats:
                print ("This seat is already taken!")
            elif tuple_seats[0] >= 10 or tuple_seats[1] >= 10:
                print ("Lol...NO!")
            else:
                print ("OKAY")
                print (tuple_seats)
                self.chosen_seats.append(tuple_seats)
                counter += 1

        movie_name = self.__cinema.get_movie(self.chosen_movie_id)

        print ("This is your reservation:")
        print ("Movie: {}".format(movie_name))
        print ("Date and Time: ")
        print ("Seats: {}".format(self.chosen_seats))

    def finalize_reservation(self, username, proj_id, chosen_seats):
        for i in chosen_seats:
            self.__cinema.add_reservation(
                username, proj_id, int(i[0]), int(i[1]))
        self.__cinema.database.commit()
        print ("Thanks.")

    def cancel_reservation(self, username, proj_id):
        self.__cinema.delete_reservation(username, proj_id)

    @staticmethod
    def exit():
        sys.exit()

    @staticmethod
    def help():
        print ("The commands you can use are: ")
        print ("show movies")
        print ("show movie projections")
        print ("make reservation")
        print ("finalize")
        print ("cancel reservation")
        print ("exit")

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

    def start(self):
        while True:
            command = input("Enter command: ")
            self.__command_dispatcher(command)

    def __command_dispatcher(self, command):
        # elif command == "show movie projections":

        if command == "show movies":
            self.show_movies()
        elif "show movie projections" in command:
            bam = command.split(" ")
            self.show_movie_projections(bam[3])
        elif command in "make reservation":
            self.make_reservation()
        elif command == "finalize":
            self.finalize_reservation(
                self.username, self.chosen_proj_id, self.chosen_seats)
        elif "cancel reservation" in command:
            opa = command.split(" ")
            self.cancel_reservation(opa[2], opa[3])
        elif command == "help":
            CommandInterface.help()
        elif command == "exit":
            CommandInterface.exit()
        else:
            print ("Invalid command!")
