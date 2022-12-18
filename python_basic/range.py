import sys

list(range(5)) # [0, 1, 2, 3, 4]
range(5) # range(0, 5)
type(range(5)) # <class 'range'>
for i in range(5):
    print(i, end= ' ') # 0 1 2 3 4

# 숫자 100만개를 생성하는 2가지 방법
a = [n for n in range(100000)]
b = range(100000)
len(a) # [1 ... 100000]
len(b) # range(0, 100000) => generator를 사용한다, 생성 조건만 보관.
# a 에는 이미 생성된 값이 담겨 있고, b는 생성해야만 하는 조건만 존재한다.

len(a) == len(b) # True
type(b) # <class 'range'> range()는 range 클래스를 사용

# 메모리 점유율 비교
sys.getsizeof(a) # 800984
sys.getsizeof(b) # 48
# 100만개가 아니라 1억개라도 range() 를 사용한 b의 점유율은 동일.

b[999] # 999
# 인덱스로 접근시에는 바로 생성하도록 구현

