class Calc_class14():
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y
    def div(self):
        if self.num2 == 0:
            print("나눗셈연산은 0으로 나누기가 불가능합니다. 다시 입력하세요.")
        else:
            return self.num1 /self.num2
    def squ(self):
        return self.num1**self.num2
    
    @classmethod # 엣 / 다음 메서드 한정으로 
    def filter(cls, str):
        if (str.split("-")[1][0] == '1') | (str.split("-")[1][0] == '3'):
            gender = "남성"
        elif (str.split("-")[1][0] == '2') | (str.split("-")[1][0] == '4'):
            gender = "여성"

        if int(str.split("-")[0][:2])>23:
            year = f'19{str.split("-")[0][:2]}'
        else :
            year = f'20{str.split("-")[0][:2]}'
            
        month = str.split("-")[0][2:4]
        day = str.split("-")[0][4:6]
        
        return print(f'{year}년 {month}월 {day}일에 출생한 {gender}입니다')
        
c1 = Calc_class14(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))
print ("나눗셈 : ",c1.div())
print ("제곱 : ",c1.squ())

Calc_class14.filter(input("주민번호입력 : "))