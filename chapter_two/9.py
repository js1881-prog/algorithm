a = int(input())
b = []
c = [0] * 7
o = 0
result = []

for i in range(0, a):
    a = list(map(int, input().split()))
    b.append(a)

for j in b:
    for k in j:
        c[k] += 1
    for n, m in enumerate(c):
        if (m >= o):
            o = m
            p = n
    if (o == 1):
        reward = p * 100
        result.append(reward)
    elif (o == 2):
        reward = 1000 + c.index(o) * 100
        result.append(reward)
    elif (o == 3):
        reward = 10000 + c.index(o) * 1000
        result.append(reward)
    c = [0] * 7
    o = 0
    p = 0

print(max(result))



        
        