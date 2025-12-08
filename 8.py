import numpy as pd # Hihi

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

    npGrid = pd.array(grid)
    return npGrid





def partOne():
    grid = readFile("boxes.txt")
    sampleGrid = [
    ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '^', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '^', '.', '^', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '^', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.', '.', '^', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '^', '.', '^', '.', '^', '.', '^', '.', '^', '.', '.', '.', '^', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]


    count = 0
    targetedRows = []
    connections = [

    ]


    for i in range(len(grid)):
        target = pd.array(grid[i])
        newGrid = grid
        newGrid.pop(i)

        ## Get distances
        diffs = newGrid - target
        # Calculate
        distances_sq = pd.sum(diffs**2, axis=1)
        # Get the smallest distance index
        closest_index = pd.argmin(distances_sq)
        # Get the closest point values
        closest_point = grid[closest_index]



        
    



    print(count)


def partTwo():
    grid = readFile("beams.txt")
    sampleGrid = [
        ['.', '.', '.', '.', '.', '.', '.', 'S', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '^', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '^', '.', '^', '.', '^', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '^', '.', '^', '.', '.', '.', '^', '.', '^', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '^', '.', '.', '.', '^', '.', '.', '.', '.', '.', '^', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '^', '.', '^', '.', '^', '.', '^', '.', '^', '.', '.', '.', '^', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]

    # Count rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Array with the same sizes as grid, each position will be number of how many timelines have beam at that position
    dp = [[0] * cols for _ in range(rows)]

    # Find S in the first row
    start_col = grid[0].index('S')
    dp[0][start_col] = 1

    # Number of finished timelines
    finished = 0

    # Go over each row
    for r in range(rows):
        # Go over each column
        for c in range(cols):
            # How many timelines havee beam
            cnt = dp[r][c]
            if cnt == 0:
                continue

            # If we're on the last row, next step would exit the bottom
            if r == rows - 1:
                finished += cnt
                continue

            # Rows under exist
            below = grid[r + 1][c]

            if below == '.':
                # Particle just continues straight down
                dp[r + 1][c] += cnt
            elif below == '^':
                # Splitter: time splits into left and right branches

                # Left branch
                if c - 1 >= 0:
                    dp[r + 1][c - 1] += cnt
                else:
                    # Falls off the left side
                    finished += cnt

                # Right branch
                if c + 1 < cols:
                    dp[r + 1][c + 1] += cnt
                else:
                    # Falls off the right side
                    finished += cnt

    print(finished)



if __name__ == "__main__":
    partOne()












