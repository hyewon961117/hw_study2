class Adress:
    def __init__(self, jumin):
        self.jumin = jumin
        self.front, self.back = self.jumin_split()
        self.birth_year = self.birth_year()

    def jumin_split(self):
        if '-' in self.jumin: 
            splited_jumin = self.jumin.split('-')
            front = splited_jumin[0]
            back = splited_jumin[1]
        else:
            front = self.jumin[0:6]
            back = self.jumin[6:13]
        return front, back

    def birth_year(self):
        birth_year = self.front[0:2]
        birth_year = int(birth_year)
        if self.back[0] == '1' or self.back[0] == '2':
            birth_year = birth_year+1900
            return birth_year
        elif self.back[0] == '3' or self.back[0] == '4':
            birth_year = birth_year+2000
            return birth_year
        else:
            return None
        
    def is_lunar_year(self):
        if self.birth_year % 400 == 0:
            return True
        elif self.birth_year % 100 == 0:
            return False
        elif self.birth_year % 4 == 0:
            return True
        else:
            return False
    def is_valid_date(self):
        month = int(self.front[2:4])
        day = int(self.front[4:6])
        if month < 1 or month > 12:
            return False

        if month in [4, 6, 9, 11]:
            if day > 30:
                return False
        elif month == 2:
            if self.is_lunar_year() and day > 29:
                return False
            elif not self.is_lunar_year() and day > 28:
                return False
        else:
            if day > 31:
                return False
        return True
        
    def is_gender_func(self):
        if self.back[0] == '1' or self.back[0] == '3':
            gender = '남자'
        elif self.back[0] == '2' or self.back[0] == '4':
            gender = '여자'
        else:
            print('잘못된 주민번호를 입력하셨습니다.')
        return gender



# jumin =  input('당신의 주민번호를 입력하세요: ')
# person = Adress(jumin)

# if person.birth_year is not None:
#     print(f'당신의 출생연도는 {person.birth_year}입니다.')
#     if person.is_lunar_year():
#         print('당신은 윤년에 태어났습니다.')
#     else:
#         print('당신은 평년에 태어났습니다.')
#     print(f'당신의 성별은 {person.is_gender_func()}입니다.')
#     if person.is_valid_date():
#         print('주민번호의 날짜 정보가 유효합니다.')
#     else:
#         print('주민번호의 날짜 정보가 유효하지 않습니다.')
# else:
#     print("주민번호가 올바르지 않습니다.")




jumin_ls = [
    '200229-3234567',
    '190229-4234567',
    '720229-1234567',
    '730229-2234567',
    '190229-5234567',
    '191629-5234567',
    '191229-523456789'
]

for jumin in jumin_ls:
    person = Adress(jumin)
    print(f'당신의 주민번호 : {jumin}')
    if person.birth_year is not None:
        print(f'당신의 출생연도는 {person.birth_year}입니다.')
        if person.is_lunar_year():
            print('당신은 윤년에 태어났습니다.')
        else:
            print('당신은 평년에 태어났습니다.')
        print(f'당신의 성별은 {person.is_gender_func()}입니다.')
        if person.is_valid_date():
            print('주민번호의 날짜 정보가 유효합니다.')
        else:
            print('주민번호의 날짜 정보가 유효하지 않습니다.')
    else:
        print("주민번호가 올바르지 않습니다.")
    print('--------------------------------------')