
from PyQt5 import QtWidgets
from GUI_main import Ui_Dialog
# from eventHandler import eventHandlerSet
import sys

if __name__ == "__main__":
    # GUI 전체 화면 실행

    # app = QtWidgets.QApplication(sys.argv)
    # Window = QtWidgets.QMainWindow()
    # # Dialog = QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(Window)
    # Window.show()
    # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    myWindow = Ui_Dialog()
    myWindow.show()
    sys.exit(app.exec_())