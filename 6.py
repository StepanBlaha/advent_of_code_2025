from pathlib import Path
# Read fresh ranges
def readLines(path):
    file_path = Path(path)
    rows = []

    with file_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:           # skip empty lines
                continue

            tokens = line.split()
            parsed_row = []

            for tok in tokens:
                # last line has * and + – keep them as strings
                if tok in ("*", "+"):
                    parsed_row.append(tok)
                else:
                    # treat everything else as an integer
                    parsed_row.append(int(tok))

            rows.append(parsed_row)
    return rows






def partOne():
    count = 0
    counts = []
    rows = readLines("6.txt")
    sampleRows = [
        [123, 328, 51, 64],
        [45, 64, 387, 23],
        [6, 98, 215, 314],
        ["*", "+", "*", "+"]
    ]

    for i in range(0, len(rows[0])):
        action = rows[len(rows)-1][i]
        cc = 0 if action == "+" else 1
        for row in rows:
            if row[0] == "+" or row[0] == "*":
                break
            if action == "+":
                cc = cc + row[i]
            else:
                cc = cc * row[i]
        counts.append(cc)
    count = sum(counts)
    print(count)

    
def build_cephalopod_numbers(nums, col):
    """
    For a given column index 'col', build the numbers in each row
    from that column to the right (inclusive).
    """
    result = []
    n_cols = len(nums[0])

    for row in nums:
        digits = row[col:n_cols]   # from this column to the right
        value = build_number(digits)
        result.append(value)

    return result





def read_grid(path: str):
    """
    Read the worksheet as raw text, preserving spaces.
    Returns a list of equally-long strings (padded with spaces on the right).
    """
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            # remove only newline, keep spaces
            lines.append(line.rstrip("\n"))

    if not lines:
        raise ValueError("Input file is empty")

    maxlen = max(len(line) for line in lines)
    # pad all lines on the right so they have the same length
    grid = [line.ljust(maxlen) for line in lines]
    return grid


def parse_problems_columns(grid, right_to_left=True):
    """
    Split the grid into 'problems', each problem is a list of column indices.
    Problems are separated by a column that is entirely spaces.
    We scan columns either left→right or right→left.
    """
    height = len(grid)
    width = len(grid[0])

    if right_to_left:
        col_indices = range(width - 1, -1, -1)
    else:
        col_indices = range(width)

    def is_blank_column(c: int) -> bool:
        # a column is blank if all characters in that column are spaces
        for r in range(height):
            if grid[r][c] != " ":
                return False
        return True

    problems = []
    current = []

    for c in col_indices:
        if is_blank_column(c):
            if current:
                problems.append(current)
                current = []
        else:
            current.append(c)

    if current:
        problems.append(current)

    # each element in problems is a list of column indices, in the order we scanned
    return problems


def build_number_from_column(grid, col: int) -> int:
    """
    For a given column index, build one number from the digits
    in that column (top to bottom, ignoring spaces).
    The bottom row is the operator row, so we skip it.
    """
    digits = []
    # all rows except the last (which holds operators)
    for r in range(len(grid) - 1):
        ch = grid[r][col]
        if ch.isdigit():
            digits.append(ch)

    if not digits:
        # if somehow no digits, treat as 0 (or raise an error if you prefer)
        return 0

    return int("".join(digits))


def get_operator_for_problem(grid, cols):
    last_row = grid[-1]
    for c in cols:
        ch = last_row[c]
        if ch != " ":
            return ch
    raise ValueError("No operator found for problem with columns: " + repr(cols))


def partTwo():
    grid = read_grid("6.txt")
    problems = parse_problems_columns(grid, right_to_left=True)

    grand_total = 0

    for cols in problems:
        op = get_operator_for_problem(grid, cols)

       
        numbers = [build_number_from_column(grid, c) for c in cols]

        if op == "+":
            result = sum(numbers)
        elif op == "*":
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operator {op!r}")

        grand_total += result

    print(grand_total)






if __name__ == "__main__":
    partTwo()
    











