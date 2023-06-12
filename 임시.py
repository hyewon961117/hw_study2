def inputValues():
    in_name = input('상품명을 입력하세요 : ')
    in_su = int(input('수량을 입력하세요 : '))
    in_dan = int(input('단가를 입력하세요 : '))
    return in_name, in_su, in_dan

x, y, z = inputValues()

print(x)
print(y)
print(z)
print(in_name)