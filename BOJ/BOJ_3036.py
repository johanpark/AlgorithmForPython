import sys
import math

n = int(input())
numList = list(map(int, input().split()))

base = numList[0]

for i in range(1, n):
    gcdNum = math.gcd(base, numList[i])
    numerator = base // gcdNum
    denominator = numList[i] // gcdNum
    print(f"{numerator}/{denominator}")