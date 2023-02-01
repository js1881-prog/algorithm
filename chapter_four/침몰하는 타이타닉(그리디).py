from collections import deque
# import sys

# sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a) # list는 pop()을 하면 시퀀스를 당겨와서 비효율적이다. 하지만 deque는 당겨오지 않고 그대로 포인터 변수가 
             # 다음을 읽어오기 때문에 더 효율적으로 사용가능

cnt = 0

while a:
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > m:
        a.pop()
        cnt += 1
    else:
        a.popleft() # deque 제일 앞의 index를 pop
        a.pop()
        cnt += 1

print(cnt)

