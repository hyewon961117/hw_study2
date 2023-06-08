class calc_class11():
   
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def div(self):
        return round(self.x / self.y,1)
    
    def squ(self):
        return self.x**self.y

print('<실행결과>')

num1 = int(input("첫번째 정수를 입력하세요 "))
num2 = int(input("두번째 정수를 입력하세요 "))

obj = calc_class11(num1, num2)
print('나눗셈', obj.div())
print('제곱', obj.squ())

