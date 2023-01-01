a, b = map(int, input().split())
q = []

for i in range(1, a + 1):
    if (a % i == 0):
        q.append(i)
        # [1, 2, 5, 10]
try:
    print(q[b - 1])
except:
    print(-1)