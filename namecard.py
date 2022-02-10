# 클래스명 정의
class Namecard:

    # 변수 초기화(클래스 호출되면 자동 실행되는 함수)
    def __init__(self, name, email, phone, address):	
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    # 참조값 대신 문자열로 출력
    def __str__(self):
        return f'이름:{self.name}, 이메일:{self.email}, 전화번호:{self.phone}, 주소:{self.address}'

    # def __repr__(self):
    #     return f'이름:{self.name}'