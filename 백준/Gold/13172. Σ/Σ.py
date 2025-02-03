import sys

input = sys.stdin.readline

M = int(input())
pseudo_prime = 1000000007

def mod_inverse(a, p):
    try_counter = p-2
    return_value = 1
    while try_counter:
        if try_counter % 2:
            return_value = (return_value*a)%p
        a = (a*a)%p
        try_counter >>= 1
    return return_value

calculated_number = 0

for i in range(M):
    N,S = map(int,input().split())
    calculated_number = (calculated_number + mod_inverse(N,pseudo_prime)*(S%pseudo_prime))%pseudo_prime

print(calculated_number)