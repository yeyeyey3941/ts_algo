def solution(gems):
    answer = []
    kind = set(gems)
    number_of_kind = len(kind)
    if number_of_kind==len(gems):
        return [1,number_of_kind]
    if number_of_kind == 1:
        return [1,1]
    all_gems = [1,len(gems)]
    current_gem = dict()
    start_pointer = 0
    for end_pointer in range(len(gems)):
        if current_gem.get(gems[end_pointer]):
            current_gem[gems[end_pointer]] += 1
        else:
            current_gem[gems[end_pointer]] = 1
        while len(current_gem)==number_of_kind and start_pointer<end_pointer:
            if all_gems[1]-all_gems[0] > end_pointer-start_pointer:
                all_gems = [start_pointer+1,end_pointer+1]
            start_pointer+=1
            current_gem[gems[start_pointer-1]] -= 1
            if not(current_gem[gems[start_pointer-1]]):
                del current_gem[gems[start_pointer-1]]
    return all_gems
