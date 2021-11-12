from collections import deque
def solution(n, computers):
    def BFS(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for j in range(n):
                if computers[i][j] and not visited[j]:
                    q.append(j)
    answer = 0
    visited = [0 for i in range(len(computers))]
    print(visited)
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
    return answer

#TestCase
n =3
computer = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computer))
#Expected Result = 2
n =3
computer = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computer))
#Excpected Result = 1