n = int(input())
result = []
for _ in range(n):
    x, y = map(int, input().split())
    mul = x * y
    while y != 0:
        if x < y:
            x, y = y, x
        x = x -y
    gcd = x
    lcm = mul // gcd
    result.append(lcm)

for i in range(len(result)):
    print(result[i])