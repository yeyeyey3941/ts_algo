x,y,w,s = map(int,input().split())

answer = 0

if 2*w > s: # 대각이동이 두번 이동보다 저렴하면
    s_count = min(x,y) # 근접 위치로 대각이동
    remain_move = x+y-2*s_count
    if s<w: # 대각이동이 한번이동보다 저렴하다면, 대각이동을 두번해서 일반이동처럼
        answer = s*s_count + 2*s*(remain_move//2) + w*(remain_move%2)
    else:
        answer = w*(remain_move) + s*s_count
else :
    answer = w*(x+y)
print(answer)