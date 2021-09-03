import sys
n = int(input())
memberList = list()
for _ in range(n):
    memberList.append(list(sys.stdin.readline().split()))
memberList.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(memberList[i][0]+' '+memberList[i][1])