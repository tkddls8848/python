answers = [1,3,2,4,2]
answer = []
sol1 = [1, 2, 3, 4, 5]
sol2 = [2, 1, 2, 3, 2, 4, 2, 5]
sol3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

correct = [0,0,0]
for i in range(0, len(answers)):
    if sol1[i % len(sol1)] == answers[i]:
        correct[0] += 1
for j in range(0, len(answers)):
    if sol2[j % len(sol2)] == answers[j]:
        correct[1] += 1
for k in range(0, len(answers)):
    if sol3[k % len(sol3)] == answers[k]:
        correct[2] += 1

max = max(correct)

for a in range(1, 4):
    if correct[a-1] == max:
        answer.append(a)

