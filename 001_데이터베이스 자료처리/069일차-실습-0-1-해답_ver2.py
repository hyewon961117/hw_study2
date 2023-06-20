# 069일차-실습-0-1-ver2
import os
import sys
import pymysql # MySQL데이터베이스를 사용하기 위한 라이브러리를 등록함
config = {                  # MySQL데이터베이스를 사용하기 위해 환경변수를 딕셔너리로 생성함. 
    'host' : '127.0.0.1',   # MySql 이 동작하는 ipv4주소 
    'user' : 'root',        # MySql 설치할 때 정한 계정 
    'passwd' : '0000',  # MySql 설치할 때 정한 비밀번호
    'database' : 'work', # MySql 설치할 때 처음 생성한 데이터베이스
    'port' : 3306,   # MySql이 응용프로그램과 통신할 때 사용하는 포트번호 리터럴이 아닌 정수값으로 써야함
    'charset' : 'utf8',     # 한글을 사용하겠다는 설정 
    'use_unicode' : True    # 한글을 사용하겠다는 설정 
    }
#--------------------------
# 069일차-실습-0-1-해답-ver1에서는 허수아비임 / 069일차-실습-0-1-해답-ver2의 217 line 에서 사용함 
#
class InputFilter :
    def __init__(self):   
        self.inputValueFilter_result = False
        self.name = ''
        self.su = 0
        self.dan = 0
    def setName(self, name) :
        if name == '' or len(name) < 0 :
            print("공백일때 "+str(name)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.name = name
        return self.inputValueFilter_result

    def setSu(self, su) :
        if su == 0 or su < 0 :
            print("0 이거나 음수일때 "+str(su)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.su = su
        return self.inputValueFilter_result

    def setDan(self, dan) :
        if dan == 0 or dan < 0 :
            print("0나 음수일때 "+str(dan)+" 의 정보는 부정확합니다.")
            self.inputValueFilter_result = False
        else:
            self.inputValueFilter_result = True
            self.dan = dan
        return self.inputValueFilter_result
#        
#
#--------------------------
class GoodsFind :
    def __init__(self,find_sel,find_in_data=''):   
        #print('\n',sel)        
        self.read_sel = find_sel
        if find_sel == 3 or find_sel == 5 or find_sel == 6: 
            self.find_sql = "select * from goods where code =" + f"'{find_in_data}'"
        elif find_sel == 4 : 
            self.find_sql = "select * from goods where name =" + f"'{find_in_data}'"
        else :
            self.find_sql = "select * from goods"
    def goodsfind(self) :
        try :
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            cursor = conn.cursor()       # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            cursor.execute(self.find_sql)
            return cursor.fetchall()    # select 쿼리문의 실행 결과를 return함
                                        # 쿼리의 실행결과가 없으면 요소의 갯수가 0인 리스트가 반환됨
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
#--------------------------
def goodsDelete() :
    os.system('cls')
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    for row in rows :
        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
    try :
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        cursor = conn.cursor()       # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        print("<<<삭제할 상품의 코드를 입력하세요>>>")
        in_code = int(input('삭제할 코드 입력 : '))
        sql = f"select * from goods where code = {in_code}"
        cursor.execute(sql) # sql문 실행 
        rows = cursor.fetchall()
        if rows :
            sql = f"delete from goods where code = {in_code}"
            cursor.execute(sql) # sql문 실행
            conn.commit() 
            print('삭제 성공했습니다.')
            os.system("pause")
        else :
            print('삭제 실패했습니다.')
            os.system("pause")
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    for row in rows :
        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
#--------------------------
def goodsUpdate() :
    os.system('cls')
    print("<<<상품 수정입니다>>>")
    in_code = int(input('수정할 상품코드를 입력하세요 : '))
    up1 = GoodsFind(5,in_code)
    rows = up1.goodsfind()
    #
    try :
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        cursor = conn.cursor()       # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        if rows : # select 쿼리 실행결과가 있는 경우
            print("<<<상품코드 조회결과입니다>>>")
            for row in rows :
                print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
            yesNo = input('수정하시겠습니까>(y/n) : ')
            if yesNo == "y" or yesNo == "Y":
                print("<<<수정할 내용을 입력하세요.>>>")
                iValue = userInput()  # 위의 주석부분을 대체한것 
                sql = f"update goods set name = '{iValue[0]}' ,su = {iValue[1]} ,dan={iValue[2]} where code = {in_code}" 
                cursor.execute(sql) # sql문 실행
                conn.commit() 
                print("<<<수정을 완료했습니다>>>")
                print("<<<상품 수정 결과입니다>>>")
                print("{} {} {} {} ".format(int(in_code),iValue[0],int(iValue[1]),int(iValue[2])    ))
            else:
                print("<<<수정을 취소했습니다.>>>")
        else : # select 쿼리 실행결과가 없는 경우
            print('수정할 코드가 없습니다.')
            pass
    except Exception as e :
        print('db 연동 실패 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
#--------------------------
class GoodsRead :
    def __init__(self,read_sel): # 생성자 : read_sel : 코드/상품명/all ,            
        self.read_sel = read_sel
        if read_sel == '코드' :  
            self.read_sql = "select * from goods where code ="
        elif read_sel == '상품명' : 
            self.read_sql = "select * from goods where name ="
        else :
            self.read_sql = "select * from goods"
    def goodsReadOne(self) :
        try :
            conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
            cursor = conn.cursor()   # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
            #
            rows = []
            os.system('cls')

            if self.read_sel == '코드' :
                print("<<<상품 개별 조회({})입니다>>>".format(self.read_sel))
                in_code = int(input("조회할"+self.read_sel+"를 입력하세요 : "))
                sql = self.read_sql + f"'{in_code}'"
            elif self.read_sel == '상품명' : 
                print("<<<상품 개별 조회({})입니다>>>".format(self.read_sel))
                in_code = input("조회할"+self.read_sel+"를 입력하세요 : ")
                sql = self.read_sql + f"'{in_code}'"
            else :
                in_code = ''
                sql = self.read_sql
            cursor.execute(sql)
            rows = cursor.fetchall()
            if self.read_sel == '코드' or self.read_sel == '상품명' :
                if len(rows) > 0 :
                    print("===goods 테이블 조회2({})===".format(self.read_sel))
                    for row in rows :
                        print("조회결과 코드:{}, 품명:{}, 수량:{}, 단가:{} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
                else:
                    print("조회결과 입력한 {}에 맞는 상품이 없습니다".format(self.read_sel))
            else: # self.read_sel == 'all'일때
                if len(rows) > 0 :
                    print("<<<상품 목록 조회결과입니다>>>")
                    for row in rows :
                        print("{} {} {} {} ".format(int(row[0]),row[1],int(row[2]),int(row[3])    ))
                else:
                    print("조회결과 없습니다")           
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소 
        finally:
            cursor.close()
            conn.close()
#--------------------------
def tableCreate() :
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        sql = """create table goods(
            code int primary key,
            name varchar(30) not null,
            su int default 0,
            dan int default 0
            )"""
        cursor.execute(sql)
        conn.commit()
    except Exception as e :
        print("오류 : ",e)
        conn.rollback()
    finally :
        conn.close()
        cursor.close()
#--------------------------
def userInput():
    ui1 = InputFilter()
    while True:
        if ui1.setName(input("상품명을 입력하세요 : ")) :
            in_name = ui1.name
            break
        else:
            continue
    while True:
        if ui1.setSu(int(input("수량을 입력하세요 : "))) :
            in_su = ui1.su
            break
        else:
            continue
    while True:
        if ui1.setDan(int(input("단가를 입력하세요 : "))) :
            in_dan = ui1.dan
            break
        else:
            continue
    return in_name, in_su, in_dan
#--------------------------
def goodsCreate() :
    try :
        conn = pymysql.connect(**config)    # 딕셔너리 config를 인수로 사용하여 conn 객체를 만듬.
        cursor = conn.cursor()     # conn 객체로부터 cursor() 메소드를 호출하여 cursor 참조변수를 만듬.
        #
        os.system('cls')
        print("<<<상품 등록입니다>>>")
        in_code = int(input("등록할 상품코드를 입력하세요 : "))  #
        if in_code > 0 :
            c1 = GoodsFind(3,in_code) # 위의 주석부분을 대체한것 
            if len(c1.goodsfind()) :
                print("이미 존재하고 있습니다. 다른 코드를 입력하세요")
            else :
                iValue = userInput() # 위의 주석부분을 대체한것 
                #
                sql = f"insert into goods(code,name,su,dan) values({in_code},'{iValue[0]}', {iValue[1]},{iValue[2]})" 
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                print("상품등록을 성공했습니다.")
                print()
        else :
            print("상품 등록을 위해 코드를 입력해 주세요")
    except Exception as e :
        print('오류 : ', e)
        conn.rollback() # 실행 취소 
    finally:
        cursor.close()
        conn.close()
#--------------------------
def goodsReadAll() :
    os.system('cls')
    print("<<<상품 목록 조회입니다>>>")
    gf1 = GoodsFind(2)
    rows = gf1.goodsfind()
    print("===goods 테이블 조회1===")
    print("(code, name, su, dan)")
    for row in rows :
        print(row)
#--------------------------
if __name__ == "__main__" :
    tableCreate()
    while True:
        os.system('cls')
        print("---상품관리---")
        print("상품    등록 : 1 ")
        print("상품목록조회 : 2 ")
        print("코드별  조회 : 3 ")
        print("상품명별조회 : 4 ")
        print("상품    수정 : 5 ")
        print("상품    삭제 : 6 ")
        print("상품관리종료 : 9 ")
        sel = int(input("작업을 선택하세요 : "))
        if sel == 1 :
            goodsCreate()
            os.system("pause")
        elif sel == 2 :
            goodsReadAll()
            os.system("pause")
        elif sel == 3 :
            r3 = GoodsRead('코드')
            r3.goodsReadOne()
            os.system("pause")
        elif sel == 4 :
            r4 = GoodsRead('상품명')
            r4.goodsReadOne()
            os.system("pause")
        elif sel == 5 :
            goodsUpdate()
            os.system("pause")
        elif sel == 6 :
            goodsDelete()
            os.system("pause")
        elif sel == 9 :
            print("상품관리를 종료합니다. ")
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else :
            print("잘못 선택했습니다. ")
            os.system("pause")