
a = int(input())
b = list(map(int, input().split()))

c = int(input())
d = list(map(int, input().split()))

p1=p2=0
e = []

while(p1 < a and p2 < c):
    if(b[p1] <= d[p2]):
        e.append(b[p1])
        p1 += 1
    else:
        e.append(d[p2])
        p2 += 1
if p1 < a:
    print(e)
    e = e+a[p1:]
if p2 < c:
    print(e)
    e = e+d[p2:]
    
for x in e:
    print(x, end=' ')
    


