def solution(sequence, k):
    answer = [0,len(sequence)-1]
    start,end = [0,0]
    summation = sequence[0]
    while end<len(sequence):
        if summation==k:
            if end-start<answer[1]-answer[0]:
                answer = [start,end]
            elif end-start==answer[1]-answer[0]:
                if start<answer[0]:
                    answer = [start,end]
            end += 1
            if end<len(sequence):
                summation += sequence[end]
        elif summation<k:
            end += 1
            if end<len(sequence):
                summation += sequence[end]
        else:
            start += 1
            summation -= sequence[start-1]
        # print(start,end,summation)
    return answer