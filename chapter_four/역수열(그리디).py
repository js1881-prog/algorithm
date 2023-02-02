import sys

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n = int(input())
a = list(map(int, input().split()))
b = [0] * n
c = 0
cnt = 0

for i in range(n):
    for j in range(n):
        if(b[j] == 0):
            cnt += 1
        if(a[i]+1 == cnt and cnt > 0):
            b[j] = i+1
            cnt = 0
            break
        if(cnt == 1 and a[i] == 0):
            b[j] = i
            cnt = 0
            break
print(b)











