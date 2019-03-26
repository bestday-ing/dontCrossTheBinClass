import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import Crawl


class Dialog(QtWidgets.QDialog):
    def __init__(self, dinput):
        super(Dialog, self).__init__()
        self.createFormGroupBox(dinput)

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        status = QtWidgets.QLabel('아이디와 비밀번호를 입력해주세요')

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addWidget(status)
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setWindowTitle("GUI TEST") # 공백으로 수정

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
        ID = self.input_id.text()
        PWD = self.input_pwd.text()
        profile = Crawl.get_profile(ID, PWD)
        if(profile==False):
            QMessageBox.information(self, "Error", "로그인 실패!")
        else:
            #Crawl.get_major_lecture(profile)
            #크롤링 수행

    def get_output(self):
        return self._output

def init():
    login = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    login.exec_()