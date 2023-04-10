import sys
from collections import deque
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")
MAX = 10000
dis = [0] * (MAX+3)
ch = [0] * (MAX+3)
dQ = deque()
n, m = map(int, input().split())

ch[n] = 1
dis[n] = 0
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now+1, now-1, now+5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                ch[next] = 1
                dQ.append(next)
                dis[next] = dis[now] + 1

print(dis[m])