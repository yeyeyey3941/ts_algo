input = __import__("sys").stdin.readline
t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    coin_array = list(map(int, input().split()))
    coin_array.sort()
    total = int(input())
    total_array = [0]*(total+1)
    total_array[0] = 1
    for coin in coin_array:
        for i in range(0, total+1-coin):
            total_array[i+coin] += total_array[i]

    answer.append(total_array[total])


print("\n".join(map(str,answer)))