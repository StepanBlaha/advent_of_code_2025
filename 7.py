exampleGrid = [
        [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
        ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
        ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
        ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
        ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
    ]


# Read file into 2d grid
def readFile(path):
    filename = path

    with open(filename, "r", encoding="utf-8") as f:
        # 2) Build a 2D list (list of rows, each row = list of chars)
        grid = [list(line.rstrip("\n")) for line in f]

    # Now `grid` is a 2D array of characters
    # Example: access row 0, col 3:
    print(grid[0][3])

    # Print dimensions
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    print("Rows:", rows, "Cols:", cols)
    return grid





def partOne():
    grid = readFile("beams.txt")

    count = 0
    offset = 0
    beams=[]
    middle = len(grid[0]) // 2
    for i in range(0, len(grid)):



def partTwo():
    count = 0
    changed = 0 # Number of changed fields

    sampleGrid = [
        [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
        ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
        ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
        ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
        ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
    ]
    grid = readFile()
    tempGrid = grid

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    start = True # For first run 
    while changed > 0 or start == True:
        start = False
        grid = tempGrid
        changed = 0
        for i in range(rows):
            for j in range(cols):
                # only count @ cells
                if grid[i][j] == "@":
                    atC = get_mine_count(grid, i, j)
                    if atC < 4:
                        count += 1
                        tempGrid[i][j] = "x"
                        changed = changed + 1

    print(count)



if __name__ == "__main__":
    partOne()












