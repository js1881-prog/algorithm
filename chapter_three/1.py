a = int(input())
b = []
cnt = 0
for i in range(0, a):
    c = list(input().split())
    b.append(c)

for x in b:
    for y in x:
        cnt += 1
        c = y[::-1].lower()
        d = y[::].lower()
        
        if (d == c):
            print(f"#{cnt} YES")
        else:
            print(f"#{cnt} NO")

