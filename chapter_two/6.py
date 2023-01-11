a = int(input())
b = list(input().split())

def digit_sum():
    result = []
    sum = 0
    d = 0

    for i in b:
        for j in i:
            m = int(j)
            sum += m
        result.append(sum)
        sum = 0

    for j, v in enumerate(result):
        if v > d:
            d = v
            e = j
    print(b[e])

digit_sum()




