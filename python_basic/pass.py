class MyClass(object):
    def method_a(self):
        pass # 상위의 메소드가 아무것도 실행하지 않으면 아래의 메소드는 오류 발생 => 아무런 처리를 안할시 pass 처리 해줘야함 
    
    def method_b(self):
        print("Method B")

c = MyClass();
