
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




def partTwo():
    import bisect
    reds = [tuple(p) for p in readPositions("tiles.txt")]
    if not reds:
        print(0); return

    # store segments instead of enumerating every intermediate point
    segs = []
    n = len(reds)
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]
        segs.append((x1, y1, x2, y2))

    # collect coords for compression (endpoints only, plus +1 breaks)
    sx = set(); sy = set()
    for x1, y1, x2, y2 in segs:
        for x in (x1, x2):
            sx.add(x); sx.add(x + 1)
        for y in (y1, y2):
            sy.add(y); sy.add(y + 1)

    # outside guard
    minx = min(min(x1, x2) for x1,_,x2,_ in segs)
    maxx = max(max(x1, x2) for x1,_,x2,_ in segs)
    miny = min(min(y1, y2) for _,y1,_,y2 in segs)
    maxy = max(max(y1, y2) for _,y1,_,y2 in segs)
    sx.add(minx - 1); sx.add(maxx + 2)
    sy.add(miny - 1); sy.add(maxy + 2)

    sx = sorted(sx); sy = sorted(sy)
    W = len(sx) - 1; H = len(sy) - 1
    def ix(x): return bisect.bisect_left(sx, x)
    def iy(y): return bisect.bisect_left(sy, y)

    # grid_val: mark cells covered by boundary segments (fill ranges in compressed coords)
    grid_val = [[0] * H for _ in range(W)]
    for x1, y1, x2, y2 in segs:
        if x1 == x2:
            cx = ix(x1)
            cy0 = iy(min(y1, y2))
            cy1 = iy(max(y1, y2))
            for cy in range(cy0, cy1 + 1):
                grid_val[cx][cy] = (sx[cx + 1] - sx[cx]) * (sy[cy + 1] - sy[cy])
        else:
            cy = iy(y1)
            cx0 = ix(min(x1, x2))
            cx1 = ix(max(x1, x2))
            for cx in range(cx0, cx1 + 1):
                grid_val[cx][cy] = (sx[cx + 1] - sx[cx]) * (sy[cy + 1] - sy[cy])

    # ...then continue with your compressed flood-fill, allowed_val, prefix sums and rectangle search...
# ...existing code...

    # flood-fill exterior
    stack = [(minx, miny)]
    exterior = {stack[0]}
    while stack:
        x, y = stack.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx < minx or nx > maxx or ny < miny or ny > maxy:
                continue
            pt = (nx, ny)
            if pt in exterior or pt in boundary:
                continue
            exterior.add(pt)
            stack.append(pt)

    # allowed = boundary ∪ interior
    allowed = boundary.union(
        (x, y)
        for x in range(minx + 1, maxx)
        for y in range(miny + 1, maxy)
        if (x, y) not in exterior
    )

    width = maxx - minx + 1
    height = maxy - miny + 1
    total_cells = width * height

    # safety: if bounding box too large, suggest compression
    MAX_CELLS = 5_000_000
    if total_cells > MAX_CELLS:
        print(f"Bounding box too large ({total_cells} cells). Consider coordinate compression.")
        return

    # build boolean grid and 2D prefix sum
    offset_x, offset_y = -minx, -miny
    grid = [[0] * (height) for _ in range(width)]
    for x, y in allowed:
        grid[x + offset_x][y + offset_y] = 1

    # prefix sums: ps[x+1][y+1] covers grid[0..x][0..y]
    ps = [[0] * (height + 1) for _ in range(width + 1)]
    for i in range(width):
        row_sum = 0
        for j in range(height):
            row_sum += grid[i][j]
            ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

    def rect_sum(x1, y1, x2, y2):
        # inputs inclusive original coords; convert to grid indexes
        gx1, gy1 = x1 + offset_x, y1 + offset_y
        gx2, gy2 = x2 + offset_x, y2 + offset_y
        # ensure order
        if gx1 > gx2:
            gx1, gx2 = gx2, gx1
        if gy1 > gy2:
            gy1, gy2 = gy2, gy1
        # prefix sum query
        return ps[gx2 + 1][gy2 + 1] - ps[gx1][gy2 + 1] - ps[gx2 + 1][gy1] + ps[gx1][gy1]

    # check every pair of red tiles as opposite corners but use rect_sum (O(1) per pair)
    reds_list = list(set(reds))
    max_area = 0
    for i in range(len(reds_list)):
        x1, y1 = reds_list[i]
        for j in range(i + 1, len(reds_list)):
            x2, y2 = reds_list[j]
            if x1 == x2 or y1 == y2:
                continue
            xmin, xmax = min(x1, x2), max(x1, x2)
            ymin, ymax = min(y1, y2), max(y1, y2)
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area <= max_area:
                continue
            if rect_sum(xmin, ymin, xmax, ymax) == area:
                max_area = area

    print(max_area)
# ...existing code...



if __name__ == "__main__":
    partTwo()












