
from PyQt5 import QtWidgets, QtCore
from PSH_GUI import GUI_main #import Ui_Dialog
# from eventHandler import eventHandlerSet


if __name__ == "__main__":
    # GUI 전체 화면 실행
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    # Dialog = QtWidgets.QDialog()
    # Dialog.setFixedSize(959, 591)   # dialog 오브젝트 창 크기 고정
    # Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    gui = GUI_main.init_()
    #ui = Ui_Dialog()
    #ui.setupUi(Dialog)

    #Dialog.show()
    #sys.exit(app.exec_())
