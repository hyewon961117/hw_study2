# 065일차-실습-0-3-해답
# 클래스 정의
class calc_class :
    # 변수 선언
    x = y = 0
    # 생성자 : 객체 생성 + [멤버변수 초기화]
    def __init__(self, a, b):
        print('~~객체 생성~~')
        self.x = a # 10
        self.y = b # 20
    # 멤버 함수(기능)
    def plus(self): # self : 멤버(변수+함수) 참조 객체
        p = self.x + self.y
        '''
        p : 지역변수
        self.x, self.y : 전역변수  
        '''
        return p
    def minus(self):
        m = self.x - self.y
        return m
# class(1) -> object(n) 생성
obj1 = calc_class(10, 20) # 생성자 -> 객체1  
#
print('plus = ', obj1.plus()) # plus =  30
print('minus =', obj1.minus()) # minus = -10
#
obj03 = calc_class(70,90)
print('plus = ', obj03.plus())
print('minus =', obj03.minus())
#
obj2 = calc_class(0,0)  # 코딩조건 가.
                        # 객체(object)를 만들고 객체의 주소를 obj2에 할당함
                        # 이 때 인수로 0,0 을 할당함

obj03.x = 200            # 코딩조건 나. 객체의 맴버변수 x에 200을 할당함
obj03.y = 50             # 코딩조건 나. 객체의 맴버변수 y에 50을 할당함

print('plus = ', obj03.plus())  # 코딩조건 다. 객체의 맴버메서드 실행
print('minus =', obj03.minus()) # 코딩조건 다. 객체의 맴버메서드 실행