# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched:
#     # Remember indentation
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")

# ----

# Magic number app

number = 7

user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("Y", "y"):
    user_number = int(input("Guess our number: "))
    if user_number == number:
        # Two sets of indentation now for the nested if
        print("You guess correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

