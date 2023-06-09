# 예제-02
# 클래스 정의
class calc_class :
    # 멤버변수 선언
    x = y = 0
    
    # 생성자 : 객체 생성 + [멤버변수 초기화]
    def __init__(self, a, b):
        print("~~객체 생성~~")
        self.x = a
        self.y = b
        
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체
        p = self.x + self.y
        return p
    
        '''
        p : 지역변수
        self.x, self.y : 전역변수
        '''
    
    def minus(self):
        m = self.x - self.y
        return m   
    
# class(1) -> object(n) 생성
obj1 = calc_class(10,20) # 생성자 -> 객체1

# object.member()
print('plus = ', obj1.plus())
print('minus = ', obj1.minus())

# 실습
# obj03 이름의 참조변수를 한 개 더 만들고 객체를 생성하세요.
# 이 때 인수로는 (70, 90)을 이용합니다.
# obj03이름의 참조변수로부터 plus(), 와 minus()메소드를 실행해 보세요.

obj03 = calc_class(70,90)
print('plus = ', obj03.plus())
print('minus = ', obj03.minus())