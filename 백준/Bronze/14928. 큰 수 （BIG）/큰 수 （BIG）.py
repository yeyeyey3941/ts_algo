number = input()
divider = 20000303
remainder = []
multiple_value = (10**9)%divider
while len(number)>9:
    judge_number = int(number[-9:])
    number = number[:-9]
    remainder.append(judge_number%divider)
answer = int(number)%divider
while remainder:
    r = remainder.pop()
    answer  = (answer*multiple_value + r)%divider
print(answer)
