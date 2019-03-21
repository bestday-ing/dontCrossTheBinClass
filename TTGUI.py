import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

def TestGUI():
 form_class = uic.loadUiType("login.ui")[0]

 class MyWindow(QMainWindow, form_class):
     def __init__(self):
         super().__init__()
         self.setupUi(self)
         self.OK.clicked.connect(self.btn_clicked)


     def btn_clicked(self):
        data="%s, %s"% (self.edit_ID.text(),self.edit_PW.text())
        self.result.setText(data)

  #if __name__ == "__main__":
 app = QApplication(sys.argv)
 myWindow = MyWindow()
 myWindow.show()
 app.exec_()


