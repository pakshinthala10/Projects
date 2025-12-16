#2d list

num_grid = [
    [1, 2, 3,],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(num_grid[2][1])

#nested for-loop

for row in num_grid:
    for col in row: 
        print(col)
        #gives us every sngle number inside the arrays inside the grid