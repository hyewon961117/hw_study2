import pymysql
import os
import sys


config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '0000',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}

# goods 기본 테이블 만들기
try : 
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute('drop table if exists goods')
    create_table_sql = ''' create table goods(
        code int primary key,
        name varchar(30) not null,
        su int default 0,
        dan int default 0)'''
    cursor.execute(create_table_sql)
    
    cursor.execute('insert into goods values(1,"선풍기", 1, 100)')
    cursor.execute('insert into goods values(2,"냉장고", 1, 200)')
    cursor.execute('insert into goods values(3,"에어콘", 1, 300)')
    
    conn.commit()
    
except Exception as e:
    print('error 발생 : ', e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()
    
# 상품 등록 함수
def insert_values():
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        text = input("code name su dan (구분자 띄어쓰기) : ")
        code = int(text.split()[0])
        name = text.split()[1]
        su = int(text.split()[2])
        dan = int(text.split()[3])
        
        insert_values_sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
        cursor.execute(insert_values_sql)
        conn.commit()
        
    except Exception as e:
        print('error 발생 : ', e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
        
# 전체 상품 조회 함수
def all_select_from():
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        cursor.execute("select * from goods")
        rows = cursor.fetchall()
        
        print('CODE, NAME, SU, DAN')
        
        for row in rows:
            print(row)
        
        print("")
        print('=> 검색된 레코드 수 : ', len(rows))
        
    except Exception as e:
        print('error 발생 : ', e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
        
# # 검색 상품 조회 함수
# def search_select_from():
#     try :
#         conn = pymysql.connect(**config)
#         cursor = conn.cursor()
        
#         search_name = input("조회할 상품명을 입력하세요 : ")
#         print("")
#         cursor.execute(f"select * from goods where name like '%{search_name}%'")
#         rows = cursor.fetchall()
        
#         if len(rows)==0:
#             print('=> 조회 결과')
#             print("검색한 상품이 없습니다.")
            
#         else:    
#             print('=> 조회 결과')
#             print('CODE, NAME, SU, DAN')
#             for row in rows:
#                 print(row)
        
#     except Exception as e:
#         print('error 발생 : ', e)
#         conn.rollback()
    
#     finally:
#         cursor.close()
#         conn.close()
        
# 코드 검색 조회 함수
def search_code_select_from():
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        search_code = int(input("조회할 상품코드를 입력하세요 : "))
        print("")
        cursor.execute(f"select * from goods where code = {search_code}")
        rows = cursor.fetchall()
        
        if len(rows)==0:
            print('=> 조회 결과')
            print("검색한 상품이 없습니다.")
            
        else:    
            print('=> 조회 결과')
            print('CODE, NAME, SU, DAN')
            for row in rows:
                print(row)
        
    except Exception as e:
        print('error 발생 : ', e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()

 
# 상품 검색 조회 함수
def search_name_select_from():
    try :
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        
        search_name = input("조회할 상품명을 입력하세요 : ")
        print("")
        cursor.execute(f"select * from goods where name like '%{search_name}%'")
        rows = cursor.fetchall()
        
        if len(rows)==0:
            print('=> 조회 결과')
            print("검색한 상품이 없습니다.")
            
        else:    
            print('=> 조회 결과')
            print('CODE, NAME, SU, DAN')
            for row in rows:
                print(row)
        
    except Exception as e:
        print('error 발생 : ', e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()


os.system('cls')
while True :
    # os.system('cls')
    print('===상품관리===')
    
    menus = ['상품    등록 : 1', '전체상품조회 : 2', '코드별  조회 : 3', '상품명  조회 : 4',
             '상품    수정 : 5', '상품    삭제 : 6', '상품관리종료 : 0']
    
    for menu in menus:
        print(menu)
    
    print("")   
    num = int(input('=> 수행할 작업의 번호를 입력하세요 : '))
    print("")    
    
    if num == 1:
        print(f'===상품등록===')
        insert_values()
        print("")
        # os.system('pause')
        
    elif num == 2:
        print(f'===전체상품조회===')
        all_select_from()
        print("")
        # os.system('pause')
    
    elif num == 3:
        print(f'===코드조회===')
        search_code_select_from()
        print("")
        # os.system('pause')

    elif num == 4:
        print(f'===상품명조회===')
        search_name_select_from()
        print("")
        # os.system('pause')
        
    elif num == 5:
        print(f'===상품수정===')
        print("해당 작업 서비스는 준비중입니다.")
        print("")
        # os.system('pause')

    
    elif num == 6:
        print(f'===상품삭제===')
        print("해당 작업 서비스는 준비중입니다.")
        print("")
        # os.system('pause')

    
    elif num == 0:
        print(f'===종료===')
        print("상품관리 서비스를 종료합니다.")
        print("이용해주셔서 감사합니다.")
        break
        
    else : 
        print("잘못 입력하셨습니다.")
        print("")
        # os.system('pause')