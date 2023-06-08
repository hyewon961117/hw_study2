class calc_class12:
    num1 = num2 = 0
    def member_clear(self,x,y):
        self.num1 = x
        self.num2 = y
    def div(self):
        return self.num1 / self.num2
    def squ(self):
        return self.num1 ** self.num2
#
c1 = calc_class12()
c1.member_clear(int(input("정수를 입력하세요:")),int(input("정수를 입력하세요:")))
print ("나눗셈 : ",c1.div())
print ("제곱 : ",c1.squ())