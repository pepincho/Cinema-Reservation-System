from create_cinema_database import CreateCinemaDatabase
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
        try:
            movie_name = self.__cinema.get_movie(movie_id)
        except:
            print ("Invalid id of movie!")
            return
        # if movie_name == -1:
        #     print ("Invalid id of movie!")
        #     return
        print ("Projection for movie {}".format(movie_name))

        projections = self.__cinema.get_all_projections(movie_id)

        for projection in projections:
            print ("{} - {} - {} - {}  ".format(projection["projection_id"],
                                                projection["projection_type"],
                                                projection["projection_date"],
                                                projection["projection_time"]))

    def show_movie_projections_date(self, movie_id, date):
        try:
            movie_name = self.__cinema.get_movie(movie_id)
            print ("Projection for movie {}".format(movie_name))

            projections = self.__cinema.get_all_projections_date(movie_id, date)
        except:
            print ("Invalid id or date of movie!")

        for projection in projections:
            print ("{} - {} - {}  ".format(projection["projection_id"],
                                           projection["projection_type"],
                                           projection["projection_time"]))

        projections = self.__cinema.get_all_projections_date(movie_id, date)

    def make_reservation(self):
        self.username = input("Enter your name: ")
        counter_tickets = int(input("Chooce number of tickets: "))

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

        while counter <= counter_tickets:
            str_seats = input("Choose seat {}: ".format(counter))
            str_seats = str_seats.split(",")
            tuple_seats = tuple([int(i) for i in str_seats])

            if tuple_seats in self.hired_seats:
                print ("This seat is already taken!")
            elif tuple_seats[0] >= 10 or tuple_seats[1] >= 10:
                print ("Lol...NO!")
            else:
                self.hired_seats.append(tuple_seats)
                self.chosen_seats.append(tuple_seats)
                counter += 1

        movie_name = self.__cinema.get_movie(self.chosen_movie_id)
        date_time_proj = self.__cinema.get_date_time_projection(
            self.chosen_proj_id)

        print ("This is your reservation:")
        print ("Movie: {}".format(movie_name))
        print ("Date and Time: {} {}".format(date_time_proj["projection_date"],
                                             date_time_proj["projection_time"]))
        print ("Seats: {}".format(self.chosen_seats))
        print ("Now you should finalize or cancel your reservation.")

    def finalize_reservation(self, username, proj_id, chosen_seats):
        for i in chosen_seats:
            self.__cinema.add_reservation(
                username, proj_id, int(i[0]), int(i[1]))
        self.__cinema.database.commit()
        print ("Thanks.")

    def cancel_reservation(self, username, proj_id):
        self.__cinema.delete_reservation(username, proj_id)
        print ("You canceled the reservation with name {} and projection id {}".format(
            username, proj_id))

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
    def generate_seats():
        rows = CreateCinemaDatabase.ROW_SIZE
        cols = CreateCinemaDatabase.COL_SIZE
        matrix = [['.' for x in range(0, cols)] for x in range(0, rows)]

        return matrix

    @staticmethod
    def get_available_seats(hired_seats):
        rows = CreateCinemaDatabase.ROW_SIZE
        cols = CreateCinemaDatabase.COL_SIZE
        available_seats = CommandInterface.generate_seats()

        for i in range(0, rows):
            for j in range(0, cols):
                if (i, j) in hired_seats:
                    available_seats[i][j] = "X"
                else:
                    available_seats[i][j] = "."

        return available_seats

    def start(self):
        CommandInterface.help()

        while True:
            command = input("Enter command: ")
            self.__command_dispatcher(command)

    def __command_dispatcher(self, command):
        if command == "show movies":
            self.show_movies()
        elif "show movie projections" in command:
            splitted_command = command.split(" ")
            if len(splitted_command) >= 5:
                self.show_movie_projections_date(
                    splitted_command[3], splitted_command[4])
            else:
                self.show_movie_projections(splitted_command[3])
        elif command in "make reservation":
            self.make_reservation()
        elif command == "finalize":
            try:
                self.finalize_reservation(
                    self.username, self.chosen_proj_id, self.chosen_seats)
            except:
                print ("You should have a reservation in order to finalize.")
        elif "cancel reservation" in command:
            splitted_command = command.split(" ")
            try:
                self.cancel_reservation(splitted_command[2], splitted_command[3])
            except:
                print ("Wrong username or projection's id.")
        elif command == "help":
            CommandInterface.help()
        elif command == "exit":
            CommandInterface.exit()
        else:
            print ("Invalid command!")
