a = list()
a = [] # a = list() 와 같다

a = [1, 2, 3] # 초기값
a # [1, 2, 3]
a.append(4)
a # [1, 2, 3, 4]

a.insert(3, 5) # 3번째 인덱스에 5를 추가
a # [1, 2, 3, 5, 4]

a.append('안녕')
a.append(True)
a #[1, 2, 3, 5, 4, '안녕', True]
# 다양한 자료형을 단일 리스트에 삽입 가능.

# 인덱스 1에서 3이전까지(인덱스3 포함X)
a[1:3] # [2, 3]

a[:3] #[1, 2, 3], 시작 인덱스 생략
a[4:] #[4, '안녕', True]
a[1:4:2] #[2, 5] , 세번째 파라미터 => Step의 의미, 단계를 2로 지정하여 두칸씩 건너뛴다.

try:
    print(a[9])
except IndexError:
        print('존재하지 않는 인덱스')  # 배열의 index가 존재하지 않을 시의 예외처리
a # [1, 2, 3, 5, 4, '안녕', True]
del a[1]
a # [1, 3, 5, 4, '안녕', True]
a.remove(3) # 해당 값을 삭제
a # [1, 5, 4, '안녕', True]
a.pop(3) # '안녕', 3번 인덱스를 스택의 pop()함수로 추출
a # [1, 5, 4, True]

a