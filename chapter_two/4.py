a = int(input())
b = list(map(int, input().split()))
result = float('inf')

average = round(sum(b) / a)
print(average)

c = list(enumerate(b))


