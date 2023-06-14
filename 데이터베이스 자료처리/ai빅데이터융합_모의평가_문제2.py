# 문제2
# 가
import pymysql

config = {                  
    'host' : '127.0.0.1',  
    'user' : 'root',        
    'passwd' : '0000',  
    'database' : 'work',  
    'port' : 3306,          
    'charset' : 'utf8',      
    'use_unicode' : True    
    }

class FilterStud():
    def __init__(self,code):
        self.code = code
        self.warning = ''
        
    def studIDFilter(self):
        try:
            int(self.code)
        except:
            self.warning += '문자열 포함 오류/'
        
        if len(self.code)!=8:
            self.warning += '전체 길이 오류/'
        
        elif (1900>int(self.code[:4])) | (int(self.code[:4])>2023):
            self.warning += '입학년도 오류/'
        
        elif (0>int(self.code[4:6])) | (int(self.code[4:6])>99):
            self.warning += '학과코드 오류/'
        
        elif (1>int(self.code[6:])) | (int(self.code[6:])>99):
            self.warning += '순번 오류/'
            
        if len(self.warning)>0:
            return True, self.warning
        else:
            return False, self.warning
        
    def juminFilter(self):
        if len(self.code)!=14:
            self.warning += f'하이픈("-") 포함 {len(self.code)}자리 오류/'
        else:
            if "-" in self.code:
                self.left = self.code.split("-")[0]
                self.right = self.code.split("-")[1]
                
                try:
                    int(self.left)
                    int(self.right)
                except:
                    self.warning += '하이픈("-") 외 문자열 포함 오류/'
                
                if len(self.left)!=6:
                    self.warning += '주민번호 앞자리(6), 뒷자리(7) 오류/'
                else:
                    self.year = self.left[:2]
                    self.month = self.left[2:4]
                    self.day = self.left[4:6]
                    self.gender = self.right[0]
                    
                    if (self.gender == '1')|(self.gender == '2'):
                        self.year = '19' + self.year
                    elif (self.gender == '3')|(self.gender == '4'):
                        self.year = '20' + self.year
                    else :
                        self.warning += '주민번호 뒷자리 첫번째 오류/'
                    
                    self.month_31 = ['01','03','05','07','08','10','12']
                    self.month_30 = ['04','06','09','11']
                    
                    if int(self.year) % 400 == 0:
                        self.month_2 = 29
                    elif int(self.year) % 100 == 0:
                        self.month_2 = 28
                    elif int(self.year) % 4 == 0 :
                        self.month_2 = 29
                    else:
                        self.month_2 = 28
                    
                    if self.month =='02':
                        if int(self.day) <= self.month_2:
                            pass
                        else:
                            self.warning += 'day오류/'
                    elif self.month in self.month_31:
                        if int(self.day) <= 31:
                            pass
                        else:
                            self.warning += 'day오류/'
                    elif self.month in self.month_30:
                        if int(self.day) <= 30:
                            pass
                        else:
                            self.warning += 'day오류/'
                    else :
                        self.warning += 'month오류/'
            else:
                self.warning += '구분자("-") 오류/'
                
        if len(self.warning)>0:
            return True, self.warning
        else:
            return False, self.warning
            

def SelectStud(studID=''):
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        if studID != '' :
            sql = f"select * from stud where studID = {studID}"
        else :
            sql = f"select * from stud"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if rows :
            print('학번      성명 주민번호1 주민번호2 주소1 주소2')
            for row in rows:
                print(row[0],row[1],row[2],row[3],row[4],row[5])
        else:
            print('학생 목록이 없습니다.')
    except Exception as e:
        print('Error 발생 :', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def InputStud():
    in_name = input("성명 : ")
    check1 = True
    while check1:
        in_jumin = input("주민등록번호((-)하이픈 포함) : ")
        ju1 = FilterStud(in_jumin)
        check1, check2 = ju1.juminFilter()
        if check1 == True:
            print('다시 입력하세요. 사유 :',check2)
    in_jumin1 = in_jumin.split("-")[0]
    in_jumin2 = in_jumin.split("-")[1]
    in_addr1 = input("주소1 : ")
    in_addr2 = input("주소2 : ")
    return in_name, in_jumin1, in_jumin2, in_addr1, in_addr2


def InsertStud():
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        print("<<<학생 등록>>>")
        check1 = True
        while check1:
            in_studID = input("학번 : ")
            ID1 = FilterStud(in_studID)
            check1, check2 = ID1.studIDFilter()
            if check1 == True:
                print('다시 입력하세요. 사유 :',check2)

        in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
        
        insert_sql = f"insert into Stud values('{in_studID}','{in_name}','{in_jumin1}','{in_jumin2}','{in_addr1}','{in_addr2}')" 
        cursor.execute(insert_sql)
        conn.commit()
        
        SelectStud(in_studID)
        print("학생 등록이 완료되었습니다.")

    except Exception as e:
        print('Error 발생 :', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def UpdateDeleteStud(code):
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        in_studID = input(f"{code}할 학번 입력 : ")
        SelectStud(in_studID)
        check = input(f"정말 {code}하시겠습니까?(Y/N) : ").lower()
        if check == 'y':
            if code == '수정':
                print(f"<<<{code}할 값 입력>>>")
                in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
                sql = f"update Stud set name='{in_name}', jumin1='{in_jumin1}', jumin2='{in_jumin2}', addr1='{in_addr1}', addr2='{in_addr2}' where studID={in_studID}"
            elif code == '삭제':
                sql = f"delete from Stud where studID={in_studID}"
            cursor.execute(sql)
            conn.commit()
            print(f'{code} 완료')
            
        else :
            print(f'{code} 취소')
    except Exception as e:
        print('Error 발생 :', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        
        
while True :
    print("<<<학생정보관리>>>")
    print("1 : 학생정보 등록")
    print("2 : 학생정보 목록")
    print("3 : 학생정보 조회")
    print("4 : 학생정보 수정")
    print("5 : 학생정보 삭제")
    print("9 : 시스템 종료")
    
    num = input("작업 번호 입력 : ")
    if num == '1':
        InsertStud()
    elif num == '2':
        SelectStud()
    elif num == '3':
        in_studID = input("조회할 학번 입력 : ")
        SelectStud(in_studID)
    elif num == '4':
        SelectStud()
        UpdateDeleteStud('수정')
    elif num == '5':
        SelectStud()
        UpdateDeleteStud('삭제')
    elif num == '9':
        print('학생정보관리 시스템을 종료합니다.')
        break
    else :
        print('잘못입력하셨습니다.')