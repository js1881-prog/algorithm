import sys
from collections import deque
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q): # 단 한개라도 참이 있으면 True
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break

print(cnt)


