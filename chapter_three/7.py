import sys
import os

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]
res = 0
s=e=a//2

for i in range(a):
    for j in range(s, e+1):
        res += b[i][j]
    if i < a//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)





