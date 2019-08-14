n, k = [int(i) for i in input().split()]
fuel = input()
total_bonus = 0

combinations = {}
for i in range(k):
    combo, bonus = input().split()
    bonus = int(bonus)
    combinations[combo] = bonus

for i in combinations:
    if fuel.__contains__(i):
        for j in range(0, len(fuel) - (len(i) - 1)):
            if fuel[j:j+len(i)] == i:
               total_bonus += combinations[i]

print(total_bonus)