import pymysql

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
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute('drop table if exists goods')
    conn.commit()
    
    create_table_sql = '''create table goods(
        code int primary key,
        name varchar(30) not null,
        su int default 0,
        dan int default 0) '''
        
    cursor.execute(create_table_sql)
    
    text = input("code name su dan (구분자 띄어쓰기) : ")
    code = int(text.split()[0])
    name = text.split()[1]
    su = int(text.split()[2])
    dan = int(text.split()[3])
    
    insert_values_sql = f"insert into goods values({code},'{name}', {su}, {dan})"
    cursor.execute(insert_values_sql)
    conn.commit()

except Exception as e:
    print('error : ', e)
