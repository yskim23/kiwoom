import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from kiwoom import Bot

# 키움 API 로그인 후 계좌 정보 확인

class MyTrading(Bot):
    def __init__(self, server=None):
        super().__init__(server)

        #사용할 변수 초기화. 계좌변수
        self.acc = None

        """
        self.api는 Bot 모듈 초기화시 생성되는 Kiwoom 인스턴스임.
        Kiwoom은 API 클래스를 상속 받음. 즉, Kiwoom과 API 클래스에 정의된 메소드를
        모두 사용할 수 있다는 의미.
        self.api.connect는 Kiwoom 클래스의 connect 함수를 호출하는 것과 동일함.

        connect 함수(메소드)는 사전에 정의된 이벤트에 signal과 slot을 연결해 주는 기능
        
        이 메소드에 저장된 정보는 이벤트에 연결된 적정한 slot을 자동으로 호출하는 
        @Connector() 데코레이터가 사용한다.

        데코레이터 기능 외에도, Kiwoom.signal(event, key)과 Kiwoom.slot(event, key)는
        이벤트에 연결된 signal이나 slot을 리턴하는 기능을 한다.
        """

        """
        아래 소스 동작 설명.
        Bot의 login 메소드로 서버에 로그인이 되면, on_event_connect 이벤트가 발생한다.
        이 이벤트가 발생하면, Server의 login 함수가 실행된다.
        connect에 키움 open api 이벤트를 이벤트에 연결하고, signal에 서버와 연동하는 
        메소드를 지정. open api 와 연동 시 event 파라미터에 지정한 이름의 이벤트가 발생하면
        후처리 메소드로 slot에 연결된 메소드가 실행된다.
        TR의 경우에는 event 파라미터에 on_receive_tr_data 지정.
        signal에는 서버에 요청하기 위한 데이터를 준비하고, 서버에 데이터를 요청하는 로직을 
        구현한 메소드를 연결.
        slot에 서버에 요청한 응답이 오면 그 데이터를 처리하는 로직이 담겨진 메소드 연결.
        """
        self.api.connect(
            event='on_event_connect',
            signal=self.login,
            slot=self.server.login
        )

    def account(self):
        # get_login_info 는 API 클래스에 정의된 함수.
        cnt = int(self.api.get_login_info('ACCOUNT_CNT')) #계좌개수
        accounts = self.api.get_login_info('ACCLIST').split(';')[:cnt]  # 계좌번호

        user_id = self.api.get_login_info('USER_ID')  # 유저아이디
        user_name = self.api.get_login_info('USER_NAME')  # 유저이름

        # 접속 서버 타입
        server = self.api.get_login_info('GetServerGubun')
        server = '모의투자' if server.strip() == '1' else '실서버'

        # 첫번 째 계좌 사용 (거래종목에 따라 확인)
        self.acc = accounts[0]

        return {  # 딕셔너리 리턴
            '계좌개수': cnt,
            '계좌번호': accounts,
            '유저아이디': user_id,
            '유저이름': user_name,
            '서버구분': server
        }


    def run(self):
        # Bot의 login() 호출
        self.login()

        # 접속 성공여부 확인
        if not self.connected():
            raise RuntimeError(f"Server NOT Connected.")
            # or you may exit script - import sys; sys.exit()

        # 계좌 정보 출력
        info = self.account() ## 딕셔너리 형태로 리턴된 결과가 info에 담겨 있음.
        print('-- 계좌 정보 --')
        for key, val in info.items():
            print(f'{key}: {val}')
        


if __name__ == '__main__':

    app = QApplication(sys.argv)

    bot = MyTrading()
    bot.run()

    win = QMainWindow()
    win.setWindowTitle('Quit!')
    win.show()
    sys.exit(app.exec())





    