import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        b = int(stack.pop())
        c = int(stack.pop())
        if x == "+":
            stack.append(b+c)
        elif x == "-":
            stack.append(c-b)
        elif x == "*":
            stack.append(b*c)
        elif x == "/":
            stack.append(c/b)

print(stack[0])