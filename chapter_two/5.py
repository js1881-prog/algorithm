a, b = map(int, input().split())
result_list = [0] * (a+b+3)
max = -2147000000

for x in range(1, a+1):
    for y in range(1, b+1):
        result_list[x+y] += 1

for i in range(a+b+1):
    if result_list[i] > max:
        max = result_list[i]

for i in range(a+b+1):
    if result_list[i] == max:
        print(i, end=' ')
        