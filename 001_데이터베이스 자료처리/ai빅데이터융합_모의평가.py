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

# def SelectStud():
#     try : 
#         conn = pymysql.connect(**config)
#         cursor = conn.cursor()
#         cursor.execute("select * from stud")
#         rows = cursor.fetchall()
#         if rows :
#             for row in rows:
#                 print(row)
#         else:
#             print('학생 목록이 없습니다.')
#     except Exception as e:
#         print('Error 발생 :', e)
#         conn.rollback()
#     finally:
#         cursor.close()
#         conn.close()
     
# def SelectStud(studID=''):
#     try : 
#         conn = pymysql.connect(**config)
#         cursor = conn.cursor()
#         if studID != '' :
#             sql = f"select * from stud where studID = {studID}"
#         else :
#             sql = f"select * from stud"
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#         if rows :
#             print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
#             for row in rows:
#                 print(row)
#         else:
#             print('학생 목록이 없습니다.')
#     except Exception as e:
#         print('Error 발생 :', e)
#         conn.rollback()
#     finally:
#         cursor.close()
#         conn.close()

def SelectStud(studID=''):
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        if studID != '' :
            sql = f"select * from stud where studID = {studID}"
        else :
            sql = f"select * from stud"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print('Error 발생 :', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        
# rows = SelectStud('1')
# if rows :
#     print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
#     for row in rows:
#         print(row)
# else:
#     print('학생 목록이 없습니다.')

def InputStud():
    in_name = input("성명 : ")
    in_jumin = input("주민등록번호((-)하이픈 포함) : ")
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
        in_studID = input("학번 : ")
        in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
        
        insert_sql = f"insert into Stud values('{in_studID}','{in_name}','{in_jumin1}','{in_jumin2}','{in_addr1}','{in_addr2}')" 
        cursor.execute(insert_sql)
        cursor.commit()
        
        rows = SelectStud(in_studID)
        print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
        for row in rows:
            print(row)
        print("학생 등록이 완료되었습니다.")

    except Exception as e:
        print('Error 발생 :', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# def UpdateStud():
#     try : 
#         conn = pymysql.connect(**config)
#         cursor = conn.cursor()
#         in_studID = input("수정할 학번 입력 : ")
        
#         rows = SelectStud(in_studID)
#         print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
#         for row in rows:
#             print(row)
            
#         update_check = input("정말 수정하시겠습니까?(Y/N) : ").lower()
        
#         if update_check == 'y':
#             print("<<<수정할 값 입력>>>")
#             in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
        
#         update_sql = f"update Stud set name='{in_name}', jumin1='{in_jumin1}', jumin2='{in_jumin2}', addr1='{in_addr1}', addr2='{in_addr2}' where studID={in_studID}"
#         cursor.execute(update_sql)
#         cursor.commit()
        
#         rows = SelectStud(in_studID)
#         print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
#         for row in rows:
#             print(row)
#         print("학생 수정이 완료되었습니다.")

#     except Exception as e:
#         print('Error 발생 :', e)
#         conn.rollback()
#     finally:
#         cursor.close()
#         conn.close()

def UpdateDeleteStud(code):
    try : 
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        in_studID = input(f"{code}할 학번 입력 : ")
        rows = SelectStud(in_studID)
        print('(학번, 성명, 주민번호1, 주민번호2, 주소1, 주소2)')
        for row in rows:
            print(row)
        check = input(f"정말 {code}하시겠습니까?(Y/N) : ").lower()
        if check == 'y':
            if code == '수정':
                print(f"<<<{code}할 값 입력>>>")
                in_name, in_jumin1, in_jumin2, in_addr1, in_addr2 = InputStud()
                sql = f"update Stud set name='{in_name}', jumin1='{in_jumin1}', jumin2='{in_jumin2}', addr1='{in_addr1}', addr2='{in_addr2}' where studID={in_studID}"
            elif code == '삭제':
                sql = f"delete from Stud where studID={in_studID}"
            cursor.execute(sql)
            cursor.commit()
            
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
        UpdateDeleteStud('수정')
    elif num == '5':
        UpdateDeleteStud('삭제')
    elif num == '9':
        print('학생정보관리 시스템을 종료합니다.')
        break
    else :
        print('잘못입력하셨습니다.')