from collections import deque
import sys
read = sys.stdin.readline
n, m, v = map(int, read().split())

def BFS(i):
    q = deque()
    q.append(i)
    while q:
        i = q.popleft()
        visitListBFS[i] = 1
        print(i, end = " ")
        for j in range(1, n + 1):
            if graph[i][j] == 1 and visitListBFS[j] == 0:
                q.append(j)
                visitListBFS[j] = 1

def DFS(i):
    visitListDFS[i] = 1
    print(i, end = " ")
    for j in range(1, n + 1):
        if graph[i][j] == 1 and visitListDFS[j] == 0:
            DFS(j)

graph = [[0] * (n + 1) for _ in range(n+1)]
visitListBFS = [0] * (n + 1)
visitListDFS = [0] * (n + 1)

for _ in range(m):
    i, j = map(int, read().split())
    graph[i][j] = graph[j][i] = 1
DFS(v)
print()
BFS(v)


