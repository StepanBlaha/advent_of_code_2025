
# Read fresh ranges
def readRanges(path):
    ranges = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            start, end = line.split("-")
            ranges.append([int(start), int(end)])
    return ranges


# Read ids
def readIds(url):
    filename = url

    with open(filename, "r", encoding="utf-8") as f:
        # Strip whitespace/ new lines and parse
        arr = [int(line.strip()) for line in f if line.strip()]

    return arr






def partOne():
    count = 0

    ranges = readRanges("ingredientRanges.txt")
    sampleRanges = [
        [3, 5],
        [10, 14],
        [16, 20],
        [12, 18]
    ]
    ids = readIds("ingredientIds.txt")
    sampleIds = [
        1, 5, 8, 11, 17, 32
    ]

    for i in ids:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                count = count + 1
                break
    print(count)

    



def partTwo():
    ranges = readRanges("ingredientRanges.txt")

    # sort by start
    ranges.sort(key=lambda r: r[0])

    merged = []
    for start, end in ranges:
        if not merged:
            merged.append([start, end])
        else:
            last_start, last_end = merged[-1]
            if start <= last_end + 1:
                # extend the last interval
                merged[-1][1] = max(last_end, end)
            else:
                # disjoint interval
                merged.append([start, end])

    # now sum lengths of merged intervals
    count = sum(end - start + 1 for start, end in merged)
    print(count)




if __name__ == "__main__":
    partTwo()












