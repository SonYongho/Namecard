from namecard import Namecard
import sqlite3

def main():
   
    try:        
        with open('addressbook.txt', 'rt') as file:     # 텍스트파일을 열어서 읽은 뒤 file이라는 변수에 리스트로 담고 파일을 닫아라 
            lines = file.readlines()                                    # file 리스트를 한 줄씩 읽어서 lines에 담아라\
            # print(lines)  
    except Exception as e:
        print('예외가 발생했습니다.', e)


    book = []

    for i in range(len(lines)):
        line = lines[i].split(',')
        namecard = Namecard(line[0], line[1], line[2], line[3])
        book_list = book.append(namecard)            
    


    
    # sqlite3 내장 모듈을 임포트 후에 connect 메서드를 통해 커넥션 객체(con)를 생성합니다.
    con = sqlite3.connect('addr.db')   # 데이터베이스 접속  # 존재하지 않는 DB파일이면 새로 생성
    print('db 연결 성공\n')
    cursor = con.cursor()   
    print('SQL 실행\n')


    # 테이블이 동일 이름으로 존재하면 지우고 다시 생성
    cursor.execute('DROP TABLE IF EXISTS tblAddr')  
    print('기존 테이블 삭제 완료\n')
    cursor.execute(""" 
        CREATE TABLE tblAddr(                             
        name CHAR(3) NOT NULL,
        email CHAR(30),
        phone CHAR(14),
        addr TEXT
    )
    """)
    print('테이블 생성 완료\n')


    for i in range(len(book)):
        print(book[i])
        cursor.execute("INSERT INTO tblAddr VALUES(?, ?, ?, ?)", (book[i].name, book[i].email, book[i].phone, book[i].address))



    con.commit()
    cursor.close()
    con.close()


main()