from collections import deque
def solution(priorities, location):
    answer = 0
    d= deque([(v,i) for i, v in enumerate(priorities)]) #배열과 배열의 위치값을 2차원배열로 만듬
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            item = d.popleft()
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer