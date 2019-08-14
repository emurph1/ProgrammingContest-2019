n, t = [int(i) for i in input().split()]
teleporters = [int(i) for i in input().split()]
number_of_ships = 0

planets = []
for i in range(n):
    planets.append([int(i) for i in input().split()])

print(planets)

# First dump
for i in planets:
    smallest_parts = min(i)
    number_of_ships += smallest_parts
    for j in i:
        i[i.index(j)] -= smallest_parts

new_planets = []
for i in teleporters:
    new_planets.append(planets[i - 1])

final_stash = [0, 0, 0]
for i in new_planets:
    for j in i:
        final_stash[i.index(j)] += j

number_of_ships += min(final_stash)

print(number_of_ships)