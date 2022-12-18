print('A1', 'B2') # A1 B2 ',' = ' '(띄워쓰기)
print('A1', 'B2', sep=',') # A1,B2 (seq 파라미터로 구분자 ',' 지정)
print('aa', end=' ') # print 함수는 자체적으로 줄 바꿈 하는데, end 파라미터로 ' '(띄워쓰기)를 주어 줄 바꿈 하지 않도록 지정
print('bb')

a = ['A', 'B'] 
print(' '.join(a)) # A B, 리스트를 출력할 때는 join()으로 묶어서 처리

idx: int = 1
fruit = "Apple"

print(idx + 1, fruit) # 2 Apple
print('{0}: {1}'.format(idx + 1, fruit)) # 2 Apple , 인덱스와 함께 사용가능
print('{}: {}'.format(idx + 1, fruit)) # 인덱스 생략 가능
print(f'{idx + 1}: {fruit}') # f-string 을 이용한 인라인 삽입 => 파이썬 3.6 이상에서만 동작
