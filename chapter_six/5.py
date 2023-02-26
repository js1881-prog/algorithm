import sys
import heapq as hq
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L, x):
    global maxx
    if x > weight or L == n:
        return
    else:
        print(x)
        if x > maxx:
            maxx = x
        DFS(L+1, x+a[L])
        DFS(L+1, x)

if __name__ == "__main__":
    a = []
    maxx = 0
    weight, n = map(int, input().split())
    for i in range(n):
        hq.heappush(a, int(input()))
    DFS(0, 0)
    print(maxx)
    