import sys

n = int(input())
customers = []

for i in range(n):
    price, delivery = map(int, input().split())
    customers.append((price, delivery))
customers.sort()

max_profit = 0
result_price = 0

for i in range(n):
    base_price = customers[i][0]
    profit = 0
    for j in range(n):
        if customers[j][0] >= base_price > customers[j][1]:
            profit += base_price - customers[j][1]
    if profit > max_profit or (max_profit == profit and result_price > base_price):
        max_profit = profit
        result_price = base_price

print(result_price)







