import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = list(map(str, input()))
stack = []
sum = 0

for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])
    else:
        stack.pop()
        if a[i-1] == "(":
            sum += len(stack)
        else:
            sum += 1
print(sum)