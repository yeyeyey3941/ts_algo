
n = int(input())
l = []
dp = [[0]*(1<<n) for i in range(n)]
for i in range(n):
    l.append(list(map(int,input().split())))
fin = (1<<n) - 1  #1<<n -1 하면 시프팅보다 -1번저 하고 시프팅함


def func(current,loc):
    #print(current,bin(loc)[2:],dp[current])
    if loc == fin: #0번째 도시에서 시작할것이고,1번부터 n번까지 다 들렷을때 같아짐 
        if l[current][0]==0:#0번째에서 시작했는데, 아직 다 들리지 않았는데 0으로 갈수 없기때문에!
            return 987654321
        else:
            #print("return",current,bin(loc)[2:],dp[current])
            return l[current][0]
    if dp[current][loc]!=0:
        return dp[current][loc]
    m = int("1111111111111111111111111111111",2) #이부분이 이해가 잘 안감. int 최댓값에서 왜 저 수를 빼는것일까,안빼도 돌아가는데..., 어차피 
    for i in range(1,n):#n-1개의 도시 탐방계획
        if (((loc&(1<<i))==0) and (l[current][i] != 0)):#내가 여태 (다음에 갈도시를) 안갔다왔고, 그 가려는 도시로 갈수있을때(!=0). 그때 코스트 계산하려고
            m = min(m,func(i,(loc | (1<<i))) + l[current][i])
            #loc|(1<<i): 다음에 i번째 도시 갔다 생각하고 갱신. func(i,~~~):갱신된 값으로 i 번째 도시까지 들린값, l[current][i] : 현재위치에서 i도시로 갈때 cost
    dp[current][loc] = m
    return dp[current][loc]


print(func(0,1))
# for i in dp:
#     print(i)