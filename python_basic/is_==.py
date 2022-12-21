import copy

a = None;

# is는 id() 값을 비교하는 함수.
# id() 함수는 인자로 객체를 입력 받고, 입력 받은 그 객체의 고유 주소 값을 반환하는 함수
# == 는 값을 비교하는 함수
if a is None:
    pass # None = null, 값 자체가 정의되어 있지 않으므로 == 연산자로 비교가 불가능, is를 사용해야함.

a = [1, 2, 3]
a == a # True
a == list(a) # True
a is a # True
a is list(a) # False 
# => 값은 동일하지만 list()로 한번 더 묶어주면, 별도의 객체로 복사가 되고 다른ID를 가지게 된다.
# 따라서 is는 False가 된다.

a = [1, 2, 3]
a == copy.deepcopy(a) # True
a is copy.deepcopy(a) # False
# copy.deepcopy()로 복사한 결과 또한 값은 같지만 ID는 다르기 때문에, ==로 비교하면 True, is로 비교하면 False가 된다.