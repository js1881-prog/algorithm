import itertools as it
import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0

for x in it.combinations(a, k):
    if (sum(x) % m) == 0:
        cnt += 1
print(cnt)