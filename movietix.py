age = int(input("Enter your age: "))
is_student = bool(input("Are you a student? True/False: "))
movie_rating = input("Enter the movie rating (G, PG, PG-13): ")
has_id = bool(input("Do you have a valid ID? True/False: "))

if has_id == True:

    if movie_rating == "G":
        ticket_price = 150
    elif movie_rating == "PG":
        if age >= 10:
            ticket_price = 150
    elif movie_rating == "R-13":
        if age >= 18:
            ticket_price = 220
        elif age >= 13:
            ticket_price = 200
            if is_student == True:
               ticket_price = ticket_price - 30
    else:
        print("Invalid movie rating. Please enter G, PG, or R-13.")

print("Movie Rating:", movie_rating, "\nAge:", age, "\nStudent:", is_student, "\nTicket Price:", ticket_price)