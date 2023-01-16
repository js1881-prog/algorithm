import sys
import os

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]
c = int(input())

for i in range(c):
    d, e, f = map(int, input().split())
    if e==0:
        for _ in range(f):
            b[d-1].append(b[d-1].pop(0)) # 리스트 뒤에 append
    else:
        for _ in range(f):
            b[d-1].insert(0, b[d-1].pop()) # 리스트 앞에 insert

s = 0
e = a
sum = 0

for i in range(a):
    for j in range(s, e):
        sum += b[i][j]
    if -i > -(a//2):
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)



        



