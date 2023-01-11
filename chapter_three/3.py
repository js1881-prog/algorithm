
a = [x for x in range(0,21)]

for i in range(0, 10):
    b, c = map(int, input().split())
    for i in range(b,c+1):
        a[b] = c
        c = c - 1
        b = b + 1


print(a)

