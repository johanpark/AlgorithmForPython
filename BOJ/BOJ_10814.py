from sys import stdin

n = int(input())
memberList = list()
for _ in range(n):
    a,b = input().split()
    memberList.append(a+' '+b)
new_table = sorted(memberList, key=lambda x: -x[0])
for i in range(n):
    print(new_table[i])