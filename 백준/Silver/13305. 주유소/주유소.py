city = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices[-1] = 0

total = 0
charge_fee = prices[0]
charge_distance = distances[0]
for i in range(1,city):
    if charge_fee<=prices[i]:
        charge_distance += distances[i]
        continue
    else:
        total += charge_fee * charge_distance
        charge_fee = prices[i]
        if i == city-1:
            charge_distance = 0
        else:
            charge_distance = distances[i]
if charge_distance != 0:
    total += charge_fee * charge_distance

print(total)