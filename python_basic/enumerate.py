a = [1, 2, 3, 2, 45, 2, 5]
a # [1, 2, 3, 2, 45, 2, 5]
enumerate(a) # <enumerate object at 0x000002E7C56A4680>
list(enumerate(a)) # [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]
# => enumerate 는 인덱스를 포함한 enumerate 객체를 리턴

b = ['a1', 'b2', 'c3']

for i in range(len(b)):
    print(i, b[i])

# 위는 아래와 같은 코드로 가능(불필요한 a[i] 조회 작업과 전체길으를 조회하여 루프를 처리하는 것을 제외)
i = 0
for v in b:
    print(i, v)
    i += 1

for i,v in enumerate(b):
    print(i, v)