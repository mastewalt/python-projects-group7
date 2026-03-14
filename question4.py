# 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	Confirms total price and asks if they want to book another movie.
# •	Ends when they say "no" and displays total bookings and cost.



def movie_booking_simulation():
    # 1. Setup available movies, showtimes, and prices
    movies = {
        "1": {"title": "Bella", "time": "18:00", "price": 15.0},
        "2": {"title": "Avatar", "time": "20:00", "price": 12.0},
        "3": {"title": "Sunset", "time": "21:00", "price": 14.0},
        "4": {"title": "Cindrella", "time": "23:00", "price": 18.0}
    }
    
    total_bookings = []
    total_cost = 0.0

    print("--- Welcome to MovieBooking Simulator ---")
    
    while True:
        # 2. Show list of available movies
        print("Available Movies:")
        for key, movie in movies.items():
            print(f"{key}. {movie['title']} | Showtime: {movie['time']} | Price: ${movie['price']:.2f}")
        
        # 3. User chooses a movie
        choice = input("Select a movie from the list with numbers : ")
        if choice not in movies:
            print("Invalid movie selection. Please try again.")
            continue
            
        selected_movie = movies[choice]
        
        # 4. User chooses number of tickets
        
        num_tickets = int(input(f"How many tickets for '{selected_movie['title']}'? "))
        if num_tickets <= 0:
            print("Number of tickets must be greater than zero.")
           
        else:
            print("Invalid input. Please enter a number.")
           
            
        # 5. Confirm total price
        cost = num_tickets * selected_movie['price']
        total_cost += cost
        total_bookings.append({
            "title": selected_movie['title'],
            "tickets": num_tickets,
            "cost": cost
        })
        
        print(f"[CONFIRMATION] {num_tickets} ticket(s) for {selected_movie['title']} booked.")
        print(f"Subtotal: ${cost:.2f}")
        
        # 6. Ask if they want to book another
        another = input("Do you want to book another movie? (yes/no): ").lower()
        if another != 'yes':
            break

    # 7. End and display total bookings
    print("\n--- Final Booking Summary ---")
    for booking in total_bookings:
        print(f"- {booking['tickets']} x {booking['title']} ($${booking['cost']:.2f})")
    print(f"Total Tickets: {sum(b['tickets'] for b in total_bookings)}")
    print(f"Total Amount Payable: ${total_cost:.2f}")
    print("Thank you for using CineBooking Simulator!")

# Run the simulation
if __name__ == "__main__":
    movie_booking_simulation()
