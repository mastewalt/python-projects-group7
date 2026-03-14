# 4)	 Movie Ticket Booking Simulation
# -	Simulate a movie theater booking system that:
# •	Shows a list of available movie titles, showtimes, and seat prices.
# •	Asks the user to choose a movie and number of tickets.
# •	Confirms total price and asks if they want to book another movie.
# •	Ends when they say "no" and displays total bookings and cost.



movies = {
    "1": {"title": "Bella", "time": "18:00", "price": 15.0},
    "2": {"title": "Avatar", "time": "20:00", "price": 12.0},
    "3": {"title": "Sunset", "time": "21:00", "price": 14.0},
    "4": {"title": "Cinderella", "time": "23:00", "price": 18.0}
}

total_bookings = {}
total_cost = 0.0

print("--- Welcome to MovieBooking Simulator ---")

while True:
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['title']} | Showtime: {movie['time']} | Price: ${movie['price']:.2f}")

    choice = input("\nSelect a movie number: ").strip()
    if choice not in movies:
        print("Invalid movie selection. Please try again.")
        continue

    selected_movie = movies[choice]
    title = selected_movie['title']

    num_input = input(f"How many tickets for '{title}'? ")
    
    if num_input.isdigit() and int(num_input) > 0:
        num_tickets = int(num_input)
        cost = num_tickets * selected_movie['price']
        total_cost += cost
        
        if title in total_bookings:
            total_bookings[title]['tickets'] += num_tickets
            total_bookings[title]['cost'] += cost
        else:
            total_bookings[title] = {
                "tickets": num_tickets,
                "cost": cost
            }

        print(f"[CONFIRMATION] {num_tickets} ticket(s) for {title} added to your cart.")
    else:
        print("Invalid number of tickets. Transaction cancelled for this movie.")
        continue

    another = input("\nDo you want to book another movie? (yes/no): ").lower().strip()
    if another != 'yes':
        break

print("\n" + "="*40)
print("       FINAL BOOKING SUMMARY")
print("="*40)

if not total_bookings:
    print("No tickets were booked.")
else:
    total_tickets = 0
    for title, details in total_bookings.items():
        total_tickets += details['tickets']
        print(f"- {details['tickets']} x {title:<12} | Subtotal: ${details['cost']:.2f}")

    print("-" * 40)
    print(f"Total Tickets: {total_tickets}")
    print(f"Total Amount Payable: ${total_cost:.2f}")

print("="*40)
print("Thank you for using MovieBooking Simulator!")
