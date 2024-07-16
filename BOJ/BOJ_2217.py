import sys
n = int(input())
numList = list()
for _ in range(n):
    num = int(input())
    numList.append(num)

numList.sort(reverse=True)

maxNum = numList[0]

for i in range(n):
    currentMax = numList[i] * (i+1)
    maxNum = max(maxNum, currentMax)

print(maxNum)