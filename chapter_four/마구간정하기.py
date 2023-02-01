import sys

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n, c = map(int, input().split())
k = []
for i in range(n):
    k.append(int(input()))

k.sort()

def Count(len):
    cnt = 1
    ep = k[0]
    for i in range(1, n):
        if(k[i] - ep >= len):
            cnt += 1
            ep = k[i]
    return cnt

lt = 1
rt = k[n-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if (Count(mid) >= c):
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
        
print(res)
        




