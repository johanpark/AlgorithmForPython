import sys
from collections import Counter
n = int(input())
cardList = (map(int, input().split(' ')))
m = int(input())
targetList = map(int, input().split(' '))
target = Counter(cardList)
