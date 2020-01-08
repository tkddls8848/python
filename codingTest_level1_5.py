s = 'Pyy'
countP = 0
countY = 0
answer = True

s = s.lower()
for i in s:
    if i == 'p':
        countP+=1
    elif i == 'y':
        countY+=1
if countP != countY:
    answer = False
print(answer)