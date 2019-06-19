import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Crawl import Crawler

class Dialog(QtWidgets.QDialog):
    def __init__(self, dinput):
        super(Dialog, self).__init__()
        self.createFormGroupBox(dinput)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        self.status = QtWidgets.QLabel('아이디와 비밀번호를 입력해주세요')

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(self.status)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setWindowTitle("로그인") # 공백으로 수정

    def createFormGroupBox(self, dinput):
        layout = QtWidgets.QFormLayout()
        self.input_id = QtWidgets.QLineEdit('')
        self.input_pwd = QtWidgets.QLineEdit('')
        self.input_pwd.setEchoMode(QLineEdit.Password)

        # self.combox1 = QtWidgets.QComboBox()
        # self.combox1.setToolTip('Hello')
        # self.combox1.addItems(['India','France','UK','USA','Germany'])
        # self.spinbox1 = QtWidgets.QSpinBox()

        for text, w in zip(dinput, (self.input_id, self.input_pwd)):
            layout.addRow(text, w)

        self.formGroupBox = QtWidgets.QGroupBox("통합정보시스템 로그인")
        self.formGroupBox.setLayout(layout)

    def accept(self):
        self.status.setText('로그인 중입니다...')
        QApplication.processEvents()        # GUI 업데이트 함수
        self.Crawl = Crawler()              # 크롬 드라이버 오브젝트 생성 및 브라우저 로드
        ID = self.input_id.text()
        PWD = self.input_pwd.text()
        self.profile = self.Crawl.get_profile(ID, PWD)      # 입력 값으로 로그인 시도
        if(self.profile==False): # 로그인 실패시,
            self.status.setText('아이디와 비밀번호를 확인해주세요.')
            QApplication.processEvents()
            QMessageBox.information(self, "Error", "로그인 실패!")
        else:                   # 로그인 성공시,
            print('로그인 성공!')
            super(Dialog, self).accept()        # 로그인 성공시 return value를 위해 super 클래스 호출

    def get_output(self):
        self.Crawl.close()      # 크롬 드라이버 종료
        return self.profile     # User profile에 대한 정보 return

def init():
    login = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    login.exec_()