def solution(targets):
    answer = 0
    sorted_targets = sorted(targets,key=lambda x: (x[0],x[1]))
    end_point = targets[0][1]
    for target in sorted_targets:
        end_point = min(end_point,target[1])
        if end_point <= target[0]:
            answer += 1
            end_point = target[1]
    return answer+1