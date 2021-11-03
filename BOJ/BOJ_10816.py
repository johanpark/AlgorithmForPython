import sys
n = int(input())
cardList = list(map(int, input().split(' ')))
m = int(input())
targetList = list(map(int, input().split(' ')))
anwerList = list()
for i in range(m):
    print(cardList.count(targetList[i]), end = ' ')