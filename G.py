n, l, r = (int(i) for i in input('').split())

asteroid_bounds = []
for i in range(n):
    a, b = (int(i) for i in input('').split())
    bounds = [a, b]
    asteroid_bounds.append(bounds)

num_coll = []
for i in range(l, r+1, 1):
    collisions = 0
    for j in asteroid_bounds:
        if j[0] <= i <= j[1]:
            collisions += 1
    num_coll.append(collisions)
print(min(num_coll))