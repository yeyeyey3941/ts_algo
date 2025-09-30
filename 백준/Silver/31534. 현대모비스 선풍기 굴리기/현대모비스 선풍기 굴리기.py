from math import pi

a,b,h = map(int,input().split(" "))
if h==0 or (a==b): # 유한하지 않은 자취 : h==0이거나 사각형이 되거나 
    print(-1)
else:
    # a:h1 = b:h1+h
    # h1 =  a*h/(b-a) # deleted_height
    # h1 + h = b*h / (b-a)
    deleted_area = (a**2+(a*h/(b-a))**2)
    remain_area = (b**2+(b*h/(b-a))**2)
    print("{:.6f}".format(abs(-deleted_area*pi + remain_area*pi))) # if a>b -> abs를 통해 부호반전