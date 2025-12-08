def read_boxes(path: str):
    points = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def part_one(path: str, k_connections: int = 1000) -> int:
    points = read_boxes(path)
    n = len(points)

    # Build all pairwise distances (squared)
    pairs = []
    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            dist_sq = dx * dx + dy * dy + dz * dz
            pairs.append((dist_sq, i, j))

    # Sort by distance
    pairs.sort(key=lambda t: t[0])

    dsu = DSU(n)

    # Connect the k shortest pairs
    for idx in range(min(k_connections, len(pairs))):
        _, i, j = pairs[idx]
        dsu.union(i, j)

    # Compute component sizes
    comp_sizes = {}
    for i in range(n):
        root = dsu.find(i)
        comp_sizes[root] = comp_sizes.get(root, 0) + 1

    sizes = sorted(comp_sizes.values(), reverse=True)
    if len(sizes) < 3:
        raise ValueError("Less than 3 circuits – unexpected for real input")

    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    result = part_one("boxes.txt", 1000)
    print(result)
