import sys
from collections import deque
#sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = input()
b = int(input())
c = []

for i in range(b):
    c.append(input())

a = deque(a)

for y in c:
    b = deque(a)
    y = deque(y)
    while y:
        if b[0] == y[0]:
            b.popleft()
            y.popleft()
            if len(b) == 0:
                print("YES")
                break
        else:
            y.popleft()
        if len(y) == 0:
            print("NO")
            break
    

        
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA    
            

