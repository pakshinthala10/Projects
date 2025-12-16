#this is a functional battleship game where the player gets 5 turns to guess the location of the ships
import random 

# the input_guess function prompts and returns the user's row and column guess 
def input_guess(grid: int, specification: str) -> int: 
    assert specification == "row" or specification == "column"
    guess = int(input(f"Guess a {specification} "))
    while guess > grid or guess < 1:
        guess = int(input(f"The grid is only {specification} by {specification}. Try again: ")) 
    return guess

#store the emojis needed to notate ships      
blue = "🟦"
red = "🟥"
white = "⬜"

def print_grid(size: int, guessrow: int, columnguess: int, correct: bool) -> None:
     row = 1
     while row <= size:
        column = 1
        row_str = ""
        while column <= size:
            if row == guessrow and column == columnguess:
                if correct: 
                    row_str += red
                else: 
                    row_str += white
            else: 
                row_str += blue
            column += 1
        print(row_str)
        row += 1

# #an alternate, albeit slightly ineffecient way to do print_grid
# def print_grid(size: int, guessrow: int, columnguess: int, correct: bool) -> None:
#     #build out grid
#     grid = []
#     row = 1
#     while row <= size: 
#         row_list = []
#         column = 1 
#         while column <= size:
#             row_list.append(blue)
#             column += 1
#         grid.append(row_list)
#         row += 1
#     # search for the guessed position and change color accordingly 
#     if correct:
#         grid[guessrow -1][columnguess -1] = red
#     else: 
#         grid[guessrow -1][columnguess -1] = white
    
#     #print the whole grid
#     for row_list in grid: 
#         row_str = " "
#         for box in row_list:
#             row_str += box
#         print(row_str)

#function that tells the user if their guess is right or not
def correct_guess(secretrow: int, secretcol:int, guessrow: int, columnguess: int) -> bool:
    if secretrow == guessrow and secretcol == columnguess:
        return True 
    else: 
        return False
    
#main function that pulls together all the smaller peices
def main(size:int, secretrow: int, secretcol:int) -> None:
    turn = 1
    max_turns = 5
    won = False
    while turn < max_turns and not won: 
        print(f"=== Turn {turn}/{max_turns} ===")
        guessrow = input_guess(size, "row")
        columnguess = input_guess(size, "column")
        is_correct = correct_guess(secretrow, secretcol, guessrow, columnguess)
        print_grid(size, guessrow, columnguess, is_correct)
        if is_correct == True:
            print(f"Hit! You won in {turn}/{max_turns}!")
            won = True
        else:
            print("Miss!")
        turn += 1
    if not won:
        print(f"X/5 - Better luck next time!")

if __name__ == "__main__":
        grid_size: int = random.randint(3, 5)
        main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))