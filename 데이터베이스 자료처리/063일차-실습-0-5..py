import pymysql

config ={
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'0000',
    'database':'work',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

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

    # 레코드 추가
    range_num = int(input('한번에 등록할 상품 개수 입력 : '))

    print("------------------------")
    print("<실행결과1>")
    print("===상품등록===")
    for i in range(range_num):
        name = input('이름 입력 : ')
        age = int(input('나이 입력 : '))
        num = int(input('번호 입력 : '))
        
        cursor.execute(f"insert tb1 values('{name}', {age}, {num})")
        conn.commit()
        
        print('회원등록을 성공했습니다.')
        print("")

    print("------------------------")
    print("<실행결과2>")
    print("===tb1 테이블 조회===")
    print('NAME, AGE, NUM')

    cursor.execute('select * from tb1;')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    print("")
    print("------------------------")
    print("<실행결과3>")
    print("===상품조회1===")

    search_name = input("조회할 이름을 입력하세요 : ")
    cursor.execute(f'select * from tb1 where name="{search_name}"')
    search_rows = cursor.fetchall()

    if len(search_rows)!=0:
        for search_row in search_rows:
            print(f'조회결과는 이름:{search_row[0]}, 나이:{search_row[1]}, 수량:{search_row[2]} 입니다.')
    else:
        print('조회결과 입력한 이름에 맞는 회원이 없습니다.')
         
    print("")
    print("------------------------")
    print("<실행결과4>")
    print("===상품조회2===")

    search_name = input("조회할 이름을 입력하세요 : ")
    cursor.execute(f'select * from tb1 where name="{search_name}"')
    search_rows = cursor.fetchall()

    if len(search_rows)!=0:
        for search_row in search_rows:
            print(f'조회결과는 이름:{search_row[0]}, 나이:{search_row[1]}, 수량:{search_row[2]} 입니다.')
    else:
        print('조회결과 입력한 이름에 맞는 회원이 없습니다.')
        
except Exception as e:
    print('error 발생 : ',e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()