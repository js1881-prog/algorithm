import sys
import os

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a, b = map(int, input().split())
c = list(map(int, input().split()))

c.sort()

lt = 0 
rt = len(c) - 1
mid = 0

while(c[mid] != b):
    mid = (lt + rt) // 2
    if (c[mid] < b):
        lt = mid + 1
    elif (c[mid] > b):
        rt = mid - 1

print(mid + 1)

