
from PyQt5 import QtWidgets
from GUI_main import Ui_Dialog
# from eventHandler import eventHandlerSet


if __name__ == "__main__":
    # GUI 전체 화면 실행
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())





