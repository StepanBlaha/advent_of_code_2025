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
    beams = set()

    # Find S
    start_col = grid[0].index('S')
    beams.add(start_col)

    # Go over each row
    for i in range(1, len(grid)):
        new_beams = set()
        # Go over the column
        for j in range(len(grid[i])):
            if j in beams and grid[i][j] == "^":
                # One beam hits a splitter -> one split event
                count += 1
                if j - 1 >= 0:
                    new_beams.add(j - 1)
                if j + 1 < len(grid[i]):
                    new_beams.add(j + 1)
            elif j in beams:
                # Just keep going straight down
                new_beams.add(j)
        beams = new_beams

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
    partTwo()












