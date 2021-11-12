from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in permutations(dungeons):
        count = 0
        fatigue = k
        i = list(i)
        for j in i:
            if (j[0] <= fatigue):
                fatigue = fatigue - j[1]
                count = count + 1
        answer = max(answer, count)
    return answer

#순열조합으로 전부 구한 뒤 브루트 포스로 돌려서 max Count를 뽑는다

k = 80
d = [[80, 20], [50, 40], [30, 10]]
print(solution(k, d))
