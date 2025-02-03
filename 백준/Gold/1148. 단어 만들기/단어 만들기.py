input = __import__("sys").stdin.readline
print = __import__("sys").stdout.write

ording_start = 65
word_list = []

while True:
    word = input().strip()
    if word == "-":
        break
    word_list.append(word)
    
while True:
    puzzle = input().strip()
    puzzle_counter = [0]*26
    puzzle_has_word = [0]*26

    if puzzle == "#":
        break
    for i in puzzle:
        puzzle_counter[ord(i)-ording_start] += 1
    for word in word_list:
        word_counter = [0]*26
        has_alphabet = set()
        has_alphabet.clear()
        for i in word:
            ord_i = ord(i)-ording_start
            word_counter[ord_i] += 1
            has_alphabet.add(i)
            if word_counter[ord_i] > puzzle_counter[ord_i]:
                break
        else:
            for a in has_alphabet:
                puzzle_has_word[ord(a)-ording_start] += 1
                
    ordered_alphabet_except_not_used = sorted([(chr(i+ording_start),puzzle_has_word[i]) for i in range(26) if puzzle_counter[i] != 0],key=lambda x: x[1],reverse=True)
    maxima = ordered_alphabet_except_not_used[0][1]; minima = ordered_alphabet_except_not_used[-1][1]
    answer = ""
    answer += "".join([i[0] for i in ordered_alphabet_except_not_used if i[1] == minima]) + " " + str(minima) + " "
    answer += "".join([i[0] for i in ordered_alphabet_except_not_used if i[1] == maxima]) + " " + str(maxima)
    print(answer+"\n")