import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication # 이벤트 처리

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn = QPushButton('버튼입니다', self) # 버튼 widget 추가
        btn.resize(btn.sizeHint()) # 글씨를 기준으로 크기를 조절해줌
        btn.setToolTip('툴팁입니다') #마우스를 가져갔을때 힌트가 뜨는것
        btn.move(20, 30) # 버튼의 위치
        btn.clicked.connect(QCoreApplication.instance().quit) # 버튼이 클릭 됐을때 연결

        self.setGeometry(300, 300, 400, 500) # 앞의 2개는 윈도우 위치, 뒤의 2개는 윈도우 크기
        self.setWindowTitle('첫 번째 예제') # 윈도우 창 이름 변경
        self.show()

    def closeEvent(self, QCloseEvent): # GUI가 꺼질때 실행되는 이벤트
        ans = QMessageBox.question(self,'종료 확인', '종료하시겠습니까?',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # self, 이름, 프롬프트, 선택지, 기본선택지
        if ans == QMessageBox.Yes:
            QCloseEvent.accpet()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv) # PyQt5는 모든 어플리케이션 오브젝트를 만들어야 함.
w = Exam() # 클래스 이름의 객체를 생성
sys.exit(app.exec_()) # 이벤트 처리를 위한 main loop