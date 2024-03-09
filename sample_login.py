import sys
# from kiwoom import Bot
from kiwoom.core import Bot

from PyQt5.QtWidgets import QApplication

class MyTradingSystem(Bot):
    def __init__(self, server=None):
        super().__init__(server)
    
    def run(self):
        print('Bot.run() 호출')
        self.login()

if __name__ == '__main__':
    
    # 통신을 위해 QApplication 이용
    app = QApplication(sys.argv)

    # 인스턴스 생성
    bot = MyTradingSystem()

    # 로그인
    bot.run()

    # 통신 유지를 위해 스크립트 종료 방지
    #   - 메인 윈도우 창을 종료하면 스크립트 종료
    #   - app.exec() 단독 실행할 경우 작업관리자로 종료
    from PyQt5.QtWidgets import QMainWindow
    win = QMainWindow()
    win.setWindowTitle('Quit!')
    win.show()
    sys.exit(app.exec())


