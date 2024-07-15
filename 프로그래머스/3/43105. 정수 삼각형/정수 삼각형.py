def solution(triangle):
    height = len(triangle)
    answer = [[0]*n for n in range(1,height+1)]
    answer[0][0] = triangle[0][0]
    for row in range(1,height):
        for col in range(len(answer[row])):
          left = answer[row-1][col-1] if col-1>=0 else 0
          right = answer[row-1][col] if col<=row-1 else 0
          answer[row][col] = triangle[row][col]+max(left,right)
    return max(answer[-1])