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

    def union(self, a: int, b: int) -> bool:
        """Union sets containing a and b.
        Returns True if a merge actually happened, False if they were already connected.
        """
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def build_sorted_pairs(points):
    """Return list of (dist_sq, i, j) sorted by distance."""
    n = len(points)
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
    pairs.sort(key=lambda t: t[0])
    return pairs


def part_one(path: str, k_connections: int = 1000) -> int:
    points = read_boxes(path)
    n = len(points)

    pairs = build_sorted_pairs(points)
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


def part_two(path: str) -> int:
    points = read_boxes(path)
    n = len(points)

    pairs = build_sorted_pairs(points)
    dsu = DSU(n)

    components = n
    last_merge_pair = None  # store indices (i, j) of the last actual merge

    for _, i, j in pairs:
        # Only count pairs that actually join two different circuits
        merged = dsu.union(i, j)
        if not merged:
            continue

        last_merge_pair = (i, j)
        components -= 1

        if components == 1:
            # All junction boxes are now in one single circuit
            break

    if last_merge_pair is None:
        raise ValueError("Graph was already connected or no merges happened")

    i, j = last_merge_pair
    x1, _, _ = points[i]
    x2, _, _ = points[j]

    return x1 * x2


if __name__ == "__main__":
    path = "boxes.txt"
    result1 = part_one(path, 1000)
    print("Part 1:", result1)

    result2 = part_two(path)
    print("Part 2:", result2)
