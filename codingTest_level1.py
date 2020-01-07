heights = [6,9,5,7,4]
answer = []
for k in range(len(heights)):
    answer.append(0)
    print(answer)

for i in range(len(heights),0,-1):
    for j in range(i-1,0,-1):
        print(i,j)
        if heights[i-1] < heights[j-1]:
            answer[i-1] = j
            print(answer)
            break





