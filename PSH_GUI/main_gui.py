import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PSH_GUI import login_popup

def Init():
    form_class = uic.loadUiType("PSH_GUI/main_gui.ui")[0]

    class MyWindow(QMainWindow, form_class):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.login_btn.clicked.connect(self.login)

        def login(self):
            dinput = ['아이디', '비밀번호']
            # Call the UI and get the inputs
            dialog = login_popup.Dialog(dinput)
            if dialog.exec_() == login_popup.Dialog.Accepted:
                KNU_id, KNU_pwd = dialog.get_output()
                print(KNU_id, KNU_pwd)  # 비밀번호 콘솔에 그대로 출력 안되게

  #if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


