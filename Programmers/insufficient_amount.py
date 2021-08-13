def solution(price, money, count):
    balance = 0
    for i in range(count + 1):
        balance = balance + (price * i)
    total = balance - money
    answer = 0 if balance < money else total
    return answer

print(solution(3, 20, 4))