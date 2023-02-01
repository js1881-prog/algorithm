import sys

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n = int(input())
k = []
cnt = 0
weight = 0

for i in range(n):
    s, e = map(int, input().split())
    k.append((s, e))
    
k.sort(reverse=True)

for f, g in k:
    if (g > weight):
        weight = g
        cnt += 1






    


    

