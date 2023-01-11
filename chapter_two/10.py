a = int(input())
b = input().split() # List<String>
cnt = 0
result = 0

for x in b:
    if(x == "1"):
        cnt += 1
        result = result + cnt
    if(x == "0"):
        cnt = 0

print(result)

