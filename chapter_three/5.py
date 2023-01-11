a, b = map(int, input().split())
c = list(map(int, input().split()))

p1=cnt=sum=0
p2=1

while(p1 != a-1):
    sum = c[p1] + c[p2]
    if (c[p1] == 3 or c[p2] == 3):
        cnt += 1
        p1 += 1
        p2 = p1 + 1
    if (b > sum):
        p2 += 1
        sum += c[p2]
    if (sum == b):
        cnt += 1
        sum = 0
        p1 += 1
        p2 = p1 + 1
    elif (sum > b):
        p1 += 1
        p2 = p1 + 1

print(cnt)



