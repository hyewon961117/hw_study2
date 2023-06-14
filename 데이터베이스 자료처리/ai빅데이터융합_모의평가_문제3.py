# 문제3
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

def SelectStud(courseID=''):
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        if courseID != '' :
            sql = f"select * from stud where courseID = {courseID}"
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


def InsertCourse():
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        print("<<<과목 등록>>>")
        check1 = True
        in_courseID = input("과목 : ")

        in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
        
        insert_sql = f"insert into Stud values('{in_courseID}','{in_name}','{in_jumin1}','{in_jumin2}','{in_addr1}','{in_addr2}')" 
        cursor.execute(insert_sql)
        conn.commit()
        
        SelectStud(in_courseID)
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
        in_courseID = input(f"{code}할 학번 입력 : ")
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
    print("<<<과목관리>>>")
    print("1 : 과목 등록")
    print("2 : 과목 목록")
    print("3 : 과목 조회")
    print("4 : 과목 수정")
    print("5 : 과목 삭제")
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
        print('과목관리 시스템을 종료합니다.')
        break
    else :
        print('잘못입력하셨습니다.')