10
a = 10
b = a
a = 11
id(10), id(a), id(b) # python에서 int와 str은 불변, 메모리의 주소값을 읽을뿐 , b,a는 값이 다르다.

a = [1, 2, 3, 4, 5]
b = a
b #[1, 2, 3, 4, 5]
a[2] = 4
a # [1, 2, 4, 4, 5]
b # [1, 2, 4, 4, 5] # python 에서 list는 가변, 위와 다르게 참조하고있는 b의 값은 변경된다. '가변'
b[3] = 6
a # [1, 2, 4, 6, 5] # 참조 변수의 값을 변경 할 경우에 a의 값도 변한다.
