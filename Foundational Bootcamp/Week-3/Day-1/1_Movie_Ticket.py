class MovieTicket:
    def __init__(self, movie_name, seats):
        if seats <= 0:
            print("Seats must be greater than 0")
        self.movie_name=movie_name
        self.seats=seats

    def book_ticket(self, tickets):
        if tickets<=0:
            print("Invalid number of tickets")
        elif tickets>self.seats:
            print("Not enough seats available")
        else:
            self.seats-=tickets
            print(f"{tickets} ticket booked successfully")
            print(f"Remaining seats: {self.seats}")

movie_name=input("Enter movie name: ")
seats=int(input("Enter available seats: "))
movie=MovieTicket(movie_name, seats)
while True:
    print("Choose one  :  1. Book Ticket ,2. Exit")
    print()
    option=int(input("Enter option: "))
    if option==1:
        tickets=int(input("Enter number of tickets: "))
        movie.book_ticket(tickets)
    elif option==2:
        print("Thank You")
        break
    else:
        print("Invalid Option")