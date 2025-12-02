import math
def partOne():
    temp = 50
    count = 0

    with open("first.txt") as file:
        for line in file:
            raw = line.strip()
            if not raw:
                continue

            letter = raw[0] # "L" or "R"
            number = int(raw[1:]) # the distance

            if letter == "L":
                temp = (temp - number) % 100
            elif letter == "R":
                temp = (temp + number) % 100
            else:
                raise ValueError(f"Unknown direction: {letter}")

            if temp == 0:
                count += 1

    print(count)


def partTwo():
    pos = 50 
    count = 0 
    
    with open("first.txt") as file:
        for line in file:
            raw = line.strip()
            if not raw:
                continue

            letter = raw[0]
            steps = int(raw[1:])

            # How many times do we hit 0 during THIS rotation?
            if letter == "R":
                # Number of passes 
                k0 = (100 - pos) % 100
                if k0 == 0:
                    k0 = 100
                # No passes of 0
                if steps < k0:
                    passes = 0
                else:
                    # Count passes
                    passes = 1 + (steps - k0) // 100
                # Get new position
                pos = (pos + steps) % 100

            elif letter == "L":
                # Number of passes
                k0 = pos if pos != 0 else 100
                if steps < k0:
                    passes = 0
                else:
                    # Count passes
                    passes = 1 + (steps - k0) // 100
                # Get new position
                pos = (pos - steps) % 100

            else:
                raise ValueError(f"Unknown direction: {letter}")
            # Update count
            count += passes

    print(count)


if __name__ == "__main__":
    partTwo()
