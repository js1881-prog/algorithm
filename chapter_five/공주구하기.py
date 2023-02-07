import sys
from collections import deque
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a, b = map(int, input().split())
a = deque([_ for _ in range(1, a+1)])
cnt = 0

while len(a)!=1:
    print(a)
    a.append(a.popleft())
    if cnt == b:
        a.popleft()
        cnt = 0
    cnt += 1

print(a[0])

