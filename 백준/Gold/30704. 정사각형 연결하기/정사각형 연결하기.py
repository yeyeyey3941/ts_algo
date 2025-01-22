input = __import__('sys').stdin.readline
print = __import__('sys').stdout.write

# answer = []

T = int(input())
for _ in range(T):
    n = int(input())
    one_side = int(n**0.5)
    if n == one_side**2:
        print(f"{4*one_side}\n")
        # answer.append((n,4*one_side))
    elif n<=one_side*(one_side+1):
        print(f"{4*one_side+2}\n")
        # answer.append((n,4*one_side+2))
    else:
        print(f"{4*one_side+4}\n")
        # answer.append((n,4*one_side+4))

# print(answer)