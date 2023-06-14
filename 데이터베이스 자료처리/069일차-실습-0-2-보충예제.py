
while True : 
    jumin = input("주민등록번호 입력 : ")
    
    if len(jumin)==14:
        if "-" in jumin:
            left = jumin.split("-")[0]
            right = jumin.split("-")[1]
            try:
                int(left)
                int(right)
            except:
                print("주민등록번호는 숫자로 다시 입력하세요.")
                break
            
            if len(left)!=6:
                print("주민등록번호 앞자리는 6글자입니다.")
                break
            elif len(right)!=7:
                print("주민등록번호 뒷자리는 7글자입니다.")
                break
            else:
                pass
            year = left[:2]
            month = left[2:4]
            day = left[4:]
            gender = right[0]
            
            if (gender == '1')|(gender == '2'):
                year = '19' + year
            elif (gender == '3')|(gender == '4'):
                year = '20' + year
            else :
                print('주민등록번호 뒷자리를 확인하세요.')
                break
                
            month_31 = ['01','03','05','07','08','10','12']
            month_30 = ['04','06','09','11']
            
            if int(year) % 400 == 0:
                month_2 = 29
            elif int(year) % 100 == 0:
                month_2 = 28
            elif int(year) % 4 == 0 :
                month_2 = 29
            else:
                month_2 = 28
            
            if month =='02':
                if int(day) <= month_2:
                    pass
                else:
                    print(f"해당연도 해당월에는 {day}일이 없습니다.")
                    break
            elif month in month_31:
                if int(day) <= 31:
                    pass
                else:
                    print(f"해당연도 해당월에는 {day}일이 없습니다.")
                    break
            elif month in month_30:
                if int(day) <= 30:
                    pass
                else:
                    print(f"해당연도 해당월에는 {day}일이 없습니다.")
                    break
            else :
                print('월을 확인하세요.')
                break
            
        else :
            print("주민등록번호를 '-'로 구분하여 다시 입력하세요.")
            break
    else :
        print("주민등록번호는 '-'포함 14자리입니다. 다시 입력하세요.")
        break