import random as r

a = [1, 2, 3, 4, 5]
b = list(range(1, 11))
c = a + b
 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a.insert(3, 7)
a
a.pop()
a
a.pop(0)
a
a.remove(4) # 해당 값을 제거 (인덱스 X)
a.remove(7)
a.insert(1, 7)
a.insert(1,2)
a
a.remove(7) # 앞의 인덱스 먼저 제거
a
#print(a.index(7)) # 7이 몇번 인덱스에 있느냐
a.remove(4) # 해당 값을 제거 (인덱스 X)
a.remove(7)
a.insert(1, 7)
a.insert(1,2)
a

a = list(range(1, 11))
print(a)
print(sum(a)) # 55
print(max(a)) # 10
print(min(a)) # 1
r.shuffle(a)
a
a.sort(reverse=True)
a
a.clear()
a

a = [23, 12, 36, 53, 19]
for x in enumerate(a):
    print(x) # 튜플로 출력

b = (1, 2, 3, 4, 5)
print(b[0]) # 1
# b[0] = 7 # 튜플 값은 변경 불가능

a = [23, 12, 36, 53, 19]
for x in enumerate(a):
    print(x[0], x[1]) # 튜플로 출력
print()

for index, value in enumerate(a):
    print(index, value)
print()

a = [23, 12, 36, 53, 19]
# all은 전체가 다 참일때만 True, 하나라도 틀리면 False
if all(50>x for x in a):
    print("YES")
else:
    print("NO")
    # output = NO

# any는 한번이라도 x가 참이면 True, 다 틀리면 False
if any(15>x for x in a):
    print("YES")
else:
    print("NO")
    # output = YES
