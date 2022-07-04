# 1. addressbook.txt 파일에 다음과 같은 데이터가 들어 있다.

# 홍길동,hong@naver.com,010-1111-1111,서울시 강남구
# 고길동,go@naver.com,010-1111-1112,서울시 서초구
# 박길동,park@naver.com,010-1111-1113,경기도 수원시

# 2. addressbook.txt의 한 줄 데이터를 표현하는 Namecard 클래스를 모듈로 정의한다.

# 3. addressbook.txt 파일을 읽어 Namecard의 리스트를 book 변수로 참조한다. 

# 4. book 리스트 변수를 순회하여 화면에 출력한다.

# 5. book 리스트를 sqlite 데이터베이스 파일로 저장한다. 파일명은 addr.db로 한다.

# 평가기준 
# - 파이썬 기본 문법 활용능력
# - 파일 처리 능력
# - 객체 지향 프로그래밍 능력
# - 모듈과 패키지 활용능력
# - 데이터베이스 연동 능력

import sqlite3


class Namecard:
    # 변수 초기화
    def __init__(self, name, email, phone, address):	
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    # 문자열로 출력
    def __str__(self):
        return f'이름:{self.name}, 이메일:{self.email}, 전화번호:{self.phone}, 주소:{self.address}'


def main():
   
    try:        
        with open('addressbook.txt', 'rt', encoding='utf-8') as file:     # file = open('addressbook.txt', 'rt') 이 후 file.close() 한 것과 같다.
            lines = file.readlines()                                      # 한 줄씩 리스트에 담아라
            # print(type(lines))                          

    except Exception as e:
        print('예외가 발생했습니다.', e)

    book = []
    for i in range(len(lines)):
        line = lines[i].split(',')
        namecard = Namecard(line[0], line[1], line[2], line[3])
        book.append(namecard)         
        
    # sqlite3(내장 모듈)를 임포트 하여 connect 메서드를 통해 커넥션 객체(con)를 생성
    con = sqlite3.connect('addr.db')    # 데이터베이스 접속  # 존재하지 않는 DB파일이면 새로 생성
    cursor = con.cursor()               # SQL 실행
    
    cursor.execute('DROP TABLE IF EXISTS tblAddr')    # 테이블명 중복 방지    
    cursor.execute(
        """ 
        CREATE TABLE tblAddr(                             
            name CHAR(3) NOT NULL,
            email CHAR(30),
            phone CHAR(14),
            addr TEXT
        )
        """
    )
        
    for i in range(len(book)):
        print(book[i])
        cursor.execute("INSERT INTO tblAddr VALUES(?, ?, ?, ?)", (book[i].name, book[i].email, book[i].phone, book[i].address))
    print('------------------------------------------------------------------------------')

    cursor.execute("SELECT * FROM tblAddr")

    table = cursor.fetchall()                  

    for record in table:
        print(record)

    con.commit()
    cursor.close()
    con.close()
    

main()