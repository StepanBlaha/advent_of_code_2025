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


def readFile():
    filename = "4.txt"  # change to your file name

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


def is_around(x, y, static_x, static_y):
    # Adjacent but not the same cell
    return abs(x - static_x) <= 1 and abs(y - static_y) <= 1 and not (x == static_x and y == static_y)


def get_mine_count(field, input_y, input_x):
    axis_y = len(field)
    axis_x = len(field[0])

    count = 0
    for y in range(axis_y):
        for x in range(axis_x):
            if field[y][x] == "@" and is_around(x, y, input_x, input_y):
                count += 1
    return count


def partOne():
    count = 0

    grid =readFile()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            # only count @ cells
            if grid[i][j] == "@":
                atC = get_mine_count(grid, i, j)
                if atC < 4:
                    count += 1

    print(count)



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
    partTwo()












