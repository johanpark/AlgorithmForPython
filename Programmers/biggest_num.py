import itertools


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer
#각 배열에 3번 반복 후 재배열
# [3, 30, 34, 5, 9] -> [333, 303030, 343434, 555, 999] -> sort -> [999, 555, 343434 , 333, 303030] -> [9, 5,34, 3, 30]

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([30, 30, 98, 5, 9]))
