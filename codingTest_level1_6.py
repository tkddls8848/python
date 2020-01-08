array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

# for sentence mapping

# for command in commands:
#     a,b,c = command
#     print(a,b,c)
#     tmp = sorted(array[a - 1:b])
#     answer.append(tmp[c-1])
#
# print(answer)

# use lambda
print(list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands)))