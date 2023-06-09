import os
import sys
import pymysql

config ={
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'0000',
    'database':'test_db',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# 데이터베이스와 테이블 만들기

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute('drop database if exists test_db;')
    cursor.execute('create database test_db;')
    conn.commit()

    cursor.execute('use test_db;')
    conn.commit()

    sql = ''' create table tb1(
        name varchar(20),
        age int,
        num int);'''
        
    cursor.execute(sql)
    conn.commit()

except Exception as e:
    print('error 발생 : ',e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()

# 상품등록 함수
def insert_info():
    os.system('cls')
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    try:
        print("===상품등록===")
        # name = input('이름 입력 : ')
        # age = int(input('나이 입력 : '))
        # num = int(input('번호 입력 : '))
        info = input('이름 나이 번호 입력 (구분자 띄어쓰기) : ')
        name = info.split()[0]
        age = int(info.split()[1])
        num = int(info.split()[2])
        
        cursor.execute(f"insert tb1 values('{name}', {age}, {num})")
        conn.commit()
        
        print('회원등록을 성공했습니다.')
        print("")
    
    except Exception as e:
        print('error 발생 : ',e)
        conn.rollback()  
        
    finally:
        cursor.close()
        conn.close()

# 모든 레코드 조회 함수
def all_select_info():
    os.system('cls')
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    try: 
        print("===테이블 조회===")
        print('NAME, AGE, NUM')

        cursor.execute('select * from tb1;')
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        print("")

    except Exception as e:
        print('error 발생 : ',e)
        conn.rollback()  
        
    finally:
        cursor.close()
        conn.close()
    
# 단일 레코드 조회 함수
def one_select_info():
    os.system('cls')
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    try:
        print("===상품조회===")

        search_name = input("조회할 이름을 입력하세요 : ")
        cursor.execute(f'select * from tb1 where name="{search_name}"')
        search_rows = cursor.fetchall()

        if len(search_rows)!=0:
            for search_row in search_rows:
                print(f'조회결과는 이름:{search_row[0]}, 나이:{search_row[1]}, 수량:{search_row[2]} 입니다.')
        else:
            print('조회결과 입력한 이름에 맞는 회원이 없습니다.')
        print("")
         
        
    except Exception as e:
        print('error 발생 : ',e)
        conn.rollback()
        
    finally:
        cursor.close()
        conn.close()
        
while True :
    print("-----------------------------------")
    print("===회원관리===")
    
    menu_list = ["회원등록:1", "전체회원목록:2", "개별회원조회:3", "종료:0"]
    
    for menu in menu_list:
        print(menu)
    
    print("")
    code = int(input("=> 수행할 작업의 번호를 입력하세요 : "))
    print("")

    if code == 1:
        insert_info()
    
    elif code == 2:
        all_select_info()

    elif code == 3:
        one_select_info()
    
    elif code == 0:
        print("서비스가 종료되었습니다. 감사합니다.")
        break
    
    else : 
        print('잘못 입력했습니다.')
    