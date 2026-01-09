import sys
input = sys.stdin.readline

# ( : 0, [ : 1
answer = [] 
while True:
    s = input().rstrip()
    if s==".":
        break
    stack_list = []
    for i in s:
        if i == '(':
            stack_list.append(0)
        if i == '[':
            stack_list.append(1)
        if i == ']':
            if not stack_list:
                answer.append("no")
                break
            if stack_list[-1] == 1:
                _ = stack_list.pop()
            else:
                answer.append("no")
                break
        if i == ')':
            if not stack_list:
                answer.append("no")
                break
            if stack_list[-1] == 0:
                _ = stack_list.pop()
            else:
                answer.append("no")
                break
    else:
        if stack_list:
            answer.append("no")
        else:
            answer.append("yes")
    # print(stack_list)
print("\n".join(answer))