import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

conn = pymysql.connect(**config)
cursor = conn.cursor()

# (1) table 생성
cursor.execute("drop table if exists goods")

create_sql = '''create table goods(
    code int primary key,
    name varchar(30) not null,
    su int default 0,
    dan int default 0)'''
    
cursor.execute(create_sql)

# (5) 레코드 추가
code = int(input('코드 입력 : '))
name = input('상품명 입력 : ')
su = int(input('수량 입력 : '))
dan = int(input('단가 입력 : '))

insert_sql = f"insert into goods values({code},'{name}',{su},{dan})"
cursor.execute(insert_sql)

# (3) 레코드 수정
code = int(input('수정할 코드 입력 : '))
name = input('수정할 상품 입력 : ')
su = int(input('수정할 수량 입력 : '))
dan = int(input('수정할 단가 입력 : '))

cursor.execute(f"update goods set name = '{name}', su = {su}, dan={dan} where code={code}")
conn.commit()


