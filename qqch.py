import numpy as np

def create_arc(start, center, end, steps=5):
    arc = []
    for t in np.linspace(0, 1, steps):
        p = (1 - t) ** 2 * np.array(start) + \
            2 * (1 - t) * t * np.array(center) + \
            t ** 2 * np.array(end)
        arc.append(tuple(p))
    return arc

def round_corners(path, radius=20, steps=5):
    new_path = []
    for i in range(1, len(path) - 1):
        p1 = np.array(path[i - 1])
        p2 = np.array(path[i])
        p3 = np.array(path[i + 1])

        v1 = p2 - p1
        v2 = p3 - p2

        v1_norm = v1 / np.linalg.norm(v1)
        v2_norm = v2 / np.linalg.norm(v2)

        entry = p2 - v1_norm * radius
        exit = p2 + v2_norm * radius

        if i == 1:
            new_path.append(tuple(p1))
            new_path.append(tuple(entry))
        else:
            new_path.append(tuple(entry))

        arc_points = create_arc(entry, p2, exit, steps)
        new_path.extend(arc_points)

        if i == len(path) - 2:
            new_path.append(tuple(exit))
            new_path.append(tuple(p3))
    return new_path

original_path = [
            (75, -20),
            (75, 225),
            (725, 615),
            (150, 615),
            (150, 800)
        ]

smoothed_path = round_corners(original_path, radius=20, steps=5)

print("rounded_path = [")
for point in smoothed_path:
    print(f"    ({point[0]}, {point[1]}),")
print("]")
