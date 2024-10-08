
def solution(r1,r2):
    answer = 0
    large_circle = 0
    small_circle = 0
    large_count = 0
    small_count = 0
    for x in range(r2,0,-1):
        y = int((r2**2-x**2)**0.5)
        large_count += y+1
    large_circle = large_count*4
    for x in range(r1,0,-1):
        y = int((r1**2-x**2)**.5) if (r1**2-x**2)!=int((r1**2-x**2)**0.5)**2 else int((r1**2-x**2)**0.5)-1
        small_count += y+1
    small_circle += small_count*4
    return large_circle - small_circle