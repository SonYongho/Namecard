# 데이터베이스 확인

import sqlite3

con = sqlite3.connect('addr.db')
cursor = con.cursor()

cursor.execute("SELECT * FROM tblAddr")     # tblAddr 테이블 전체를 읽는다.

table = cursor.fetchall()                   # 테이블의 전체를 가져온다.

for record in table:
    print(record)

cursor.close()
con.close()