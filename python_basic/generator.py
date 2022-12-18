import sys

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

get_natural_number()

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

# 여러 타입의 값을 하나의 함수에서 생성
def generator():
        yield 1
        yield 'string'
        yield True
        sys.exit(0)

h = generator()
h
next(h)