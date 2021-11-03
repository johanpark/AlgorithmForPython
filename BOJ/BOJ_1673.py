import sys
for i in sys.stdin.readlines():
    k,n=map(int,i.strip().split())
    chicken = k
    while k >= n:
        chicken += k//n
        k = k//n + k%n
    print(chicken)





