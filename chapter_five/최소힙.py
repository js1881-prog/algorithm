import sys
import heapq as hq
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = []

# 최소힙입니다.
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)

print(a[0])
