import sys
import math
n, m, v = map(int, input().split())

i = v - n
ceil = math.ceil(i/(n-m))
print(ceil+1)

