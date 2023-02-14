a = [0]*10 # 1차원
a # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

b=[[0]*3 for _ in range(3)]
b[0][1] = 1
b
b[1][1] = 2
b

for x in b:
    print(x)

for x in b:
    for y in x:
        print(y, end=' ')
    print()