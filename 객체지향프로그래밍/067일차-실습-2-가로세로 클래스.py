class Rectangle():
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area_calc(self):
        self.area = self.width * self.height
        return self.area
    
    def circum_calc(self):
        self.circum = (self.width + self.height)*2
        return self.circum

print("-------------------------------------")
print('<실행결과>')
print('사각형의 넓이와 둘레를 계산합니다.')

num1 = int(input("사각형의 가로 입력 : "))
num2 = int(input("사각형의 세로 입력 : "))

rectangle = Rectangle(num1, num2)

print("-------------------------------------")
print('사각형의 넓이 :', rectangle.area_calc())
print('사각형의 둘레 :',rectangle.circum_calc())
print("-------------------------------------")