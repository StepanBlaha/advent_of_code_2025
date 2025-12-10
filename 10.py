
def readPositions(path):
    ranges = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            start, end = line.split(",")
            ranges.append([int(start), int(end)])
    return ranges



def partOne():
    count = 0

    grid = readPositions("tiles.txt")
    
    for row in grid:
        for i in range(len(grid)):
            area = ((int(row[0]) - int(grid[i][0]))+1) * ((int(row[1]) - int(grid[i][1]))+1)
            if area > count:
                count = area


    print(count)






if __name__ == "__main__":
    partOne()












