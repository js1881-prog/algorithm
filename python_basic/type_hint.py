a : str = "1"  # str임을 명시
b : int = 1 # int 임을 명시

# 이름으로 선언
a = list()
type(a) # <class 'list'>

# 기호로만 선언
type([]) # <class 'list'>
type(()) # <class 'tuple'>, tuple = immutable
type({}) # <class 'dict'>
type({1}) # <class 'set'>
