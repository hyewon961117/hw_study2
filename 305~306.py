# 패키지 import
import pymysql
print("<실행결과>")
print(pymysql.version_info)

# db연동 환경변수
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '0000',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}

try:
    # db 연동객체
    conn = pymysql.connect(**config)

    # sql문 실행 객체
    cursor = conn.cursor()

    # 테이블 조회
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    # 전체 table 목록 출력
    print(tables)

    # table 유무
    if tables:
        print('table 있음')
    else:
        print('table 없음')

except Exception as e:
    print('db error :',e)

finally:
    cursor.close()
    conn.close()