import re

b = []
a = input().lower()
a = re.findall("[0-9]", a)
print(a)
a = int("".join(a))
print(a)

print(a)

for i in range(1, a+1):
    if (a % i == 0):
        b.append(i)

print(len(b))
