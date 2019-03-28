import Crawl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, Qt
import login_popup

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())  # 창 크기 고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 윈도우 레이아웃 제거
        print('3')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        # print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    # ESC로 윈도우 종료 이벤트
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print('ESC Pressed : close app')
            self.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(959, 591)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 10, 651, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 631, 411))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 0, 501, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(660, 10, 281, 451))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listView = QtWidgets.QListView(self.frame_2)
        self.listView.setGeometry(QtCore.QRect(0, 160, 221, 281))
        self.listView.setObjectName("listView")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(5, 80, 30, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(6, 53, 30, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(6, 29, 30, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 231, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_8 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout.addWidget(self.checkBox_8)
        self.checkBox_7 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout.addWidget(self.checkBox_7)
        self.checkBox_6 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.checkBox_6)
        self.checkBox_5 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 75, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(41, 28, 221, 22))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(221, 16777215))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(6)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(7, 131, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushBt_search = QtWidgets.QPushButton(self.frame_2)
        self.pushBt_search.setGeometry(QtCore.QRect(220, 130, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBt_search.sizePolicy().hasHeightForWidth())
        self.pushBt_search.setSizePolicy(sizePolicy)
        self.pushBt_search.setObjectName("pushBt_search")



        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 130, 161, 21))
        self.plainTextEdit.setAcceptDrops(True)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setLineWidth(1)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(10, 470, 801, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 771, 21))
        self.label_2.setObjectName("label_2")

        self.pushBt_login = QtWidgets.QPushButton(self.frame_3)
        self.pushBt_login.setGeometry(QtCore.QRect(320, 40, 111, 32))
        self.pushBt_login.setObjectName("pushButton_3")

        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(260, 20, 231, 21))
        self.label_7.setObjectName("label_7")


        #########
        self.pushBt_update = QtWidgets.QPushButton(Dialog)
        self.pushBt_update.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.pushBt_update.setObjectName("pushBt_update") #update button
        #event handler 설치 : 상응하는 버튼에 설치 모듈화 하기 전 테스트로 여기 배치 나중에 다르게 빼도 괜찮음
        def updateBt_pushed():
            print("Update Btn pressed")
            Crawl.driver.quit()

        self.pushBt_update.clicked.connect(updateBt_pushed)
        #########################################################
        #########################################################
        def loginBt_pushed():
            print("Login Btn pressed")
            dinput = ['아이디', '비밀번호']
            # Call the UI and get the inputs
            dialog = login_popup.Dialog(dinput)
            if dialog.exec_() == login_popup.Dialog.Accepted:
                KNU_id, KNU_pwd = dialog.get_output()
                print(KNU_id, KNU_pwd)  # 비밀번호 콘솔에 그대로 출력 안되게

        self.pushBt_login.clicked.connect(loginBt_pushed)
        #########################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "월"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "화"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "수"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "목"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "금"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "토"))
        self.label.setText(_translate("Dialog", "Time Table"))
        self.label_3.setText(_translate("Dialog", "과목검색"))
        self.label_4.setText(_translate("Dialog", "구분"))
        self.label_5.setText(_translate("Dialog", "학년"))
        self.label_6.setText(_translate("Dialog", "학점"))
        self.checkBox_8.setText(_translate("Dialog", "*"))
        self.checkBox_7.setText(_translate("Dialog", "1"))
        self.checkBox_6.setText(_translate("Dialog", "2"))
        self.checkBox_5.setText(_translate("Dialog", "3"))
        self.checkBox_4.setText(_translate("Dialog", "4"))
        self.checkBox_3.setText(_translate("Dialog", "전공"))
        self.checkBox_2.setText(_translate("Dialog", "전공기반"))
        self.checkBox.setText(_translate("Dialog", "기본소양"))
        self.comboBox.setItemText(0, _translate("Dialog", "교수명"))
        self.comboBox.setItemText(1, _translate("Dialog", "과목명"))
        self.comboBox.setItemText(2, _translate("Dialog", "과목코드"))
        #시간 검색은 어떻게 하는 거지.??? 시간대 입력인건가????? 우리가 선택하게끔 하는 게 나을 것 같은데
        self.pushBt_search.setText(_translate("Dialog", "Search"))
        self.label_2.setText(_translate("Dialog", "졸업학점/ 이수학점"))
        self.pushBt_login.setText(_translate("Dialog", "로그인"))
        self.label_7.setText(_translate("Dialog", " 학점을 보기 위해서는 로그인이 필요합니다."))
        self.pushBt_update.setText(_translate("Dialog", "UPDATE"))



