import sys
print = sys.stdout.write


N,K,Q =  map(int,input().split())

A = list(map(int,input().split()))

X = list(map(int,input().split()))

subseqeuence = []
subseqeuence_index = [0]*N

conti_start = None
conti_end = None

for i in range(len(A)):
    if A[i] == K:
        if conti_start != None:
           subseqeuence.append(tuple([conti_start,conti_end]))
        conti_start = None
    else:
        if conti_start == None:
            conti_start = i
        conti_end = i
    subseqeuence_index[i] = len(subseqeuence)
else:
    if conti_start != None:
        subseqeuence.append(tuple([conti_start,conti_end]))

# print("subseqeuence",subseqeuence)
# print("subseqeuence_index",subseqeuence_index)

answer_string = ""

for x in X:
    ind = subseqeuence_index[x-1]
    if A[x-1] == K:
        ind -= 1
    
    if ind < 0:
        # print("0")
        answer_string += "0\n"
        continue

    if subseqeuence[ind][1] > x-1:
        last = (subseqeuence[ind][0],x-1)    
    else:
        last = subseqeuence[ind]

    print_answer = 0
    
    if ind !=0:
        for i in range(ind):
            params = (subseqeuence[i][1] - subseqeuence[i][0])+1
            print_answer += params*(params+1)//2
    params = last[1] - last[0] + 1
    print_answer += params*(params+1)//2
    # print("x:",x,"ind:",ind,"last:",last,"params:",params,"print_answer:",print_answer)
    # print(f"{print_answer}\n")
    answer_string += f"{print_answer}\n"
print(answer_string)
        