import math

n = int(input())
result = []

for _ in range(n):
    secret = input()
    sqrt = int(math.sqrt(len(secret)))
    sentence = ''
    for i in range(sqrt-1, -1, -1):
        for j in range(sqrt):
            sentence += secret[i + (j * sqrt)]
    result.append(sentence)

for res in result:
    print(res)

