#the project takes inspiration from the game Battleship
# the goal is for player 2 to guess the placement of player 1's ships

ships = ["🟦","🟦","🟦","🟦"]

p1 = int(input("Pick a secret boat location between 1 and 4: "))

if p1 > 4 or p1 < 1: 
    print("Invalid input. Please provide a number within range.")

ships[p1 - 1] = "🟥"

p2 = int(input("Guess a number between 1 and 4: "))

if p2 == p1: 
    ships[p1 - 1] = "🟥"
    print(*ships)
    print("Correct! You hit the ship.")
else: 
    ships[p1 -1] = "⬜"
    print(*ships)
    print("Incorrect! You missed the ship")
