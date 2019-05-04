from Crawl import Crawler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, Qt, pyqtSlot
import login_popup

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())  # 창 크기 고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 윈도우 레이아웃 제거
        self.profile = -1

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cell_clicked(self, row, column):
        print("Row %d and Column %d was clicked" % (row, column))  # 선택된 영역 row,col 받아오기

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
            # print('ESC Pressed : close app')  # 종료 메세지 출력
            self.close()

    def checkBoxState(self):
        msg = "select * from Course where type = "
        if self.ckBox_major.isChecked() == True:
            msg += "'공학전공'"
        if self.ckBox_Mbasic.isChecked() == True:
            msg += "'전공기반'"
        if self.ckBox_basis.isChecked() == True:
            msg += "'기본소양'"
        print(msg)

    def MoveSlider(self):
        size = self.GradeSlider.value()
        print(size)

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

        # 셀 클릭시 row col 출력
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.cellClicked.connect(self.cell_clicked)

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

        self.ckBox_grdEtc = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ckBox_grdEtc.setObjectName("checkBox_8")
        self.horizontalLayout.addWidget(self.ckBox_grdEtc)
        self.ckBox_grd1 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ckBox_grd1.setObjectName("checkBox_7")
        self.horizontalLayout.addWidget(self.ckBox_grd1)
        self.ckBox_grd2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ckBox_grd2.setObjectName("checkBox_6")
        self.horizontalLayout.addWidget(self.ckBox_grd2)
        self.ckBox_grd3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ckBox_grd3.setObjectName("checkBox_5")
        self.horizontalLayout.addWidget(self.ckBox_grd3)
        self.ckBox_grd4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.ckBox_grd4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.ckBox_grd4)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 75, 231, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ckBox_major = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.ckBox_major.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.ckBox_major)
        self.ckBox_Mbasic = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.ckBox_Mbasic.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.ckBox_Mbasic)
        self.ckBox_basis = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.ckBox_basis.setObjectName("checkBox")

        self.horizontalLayout_2.addWidget(self.ckBox_basis)
        self.GradeSlider = QtWidgets.QSlider(self.frame_2)
        self.GradeSlider.setGeometry(QtCore.QRect(41, 28, 221, 22))
        self.GradeSlider.setMaximumSize(QtCore.QSize(221, 16777215))
        self.GradeSlider.setMinimum(1)
        self.GradeSlider.setMaximum(6)
        self.GradeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GradeSlider.setInvertedAppearance(False)
        self.GradeSlider.setInvertedControls(False)
        self.GradeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.GradeSlider.setTickInterval(0)
        self.GradeSlider.setObjectName("GradeSlider")
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
        self.pushBt_update = QtWidgets.QPushButton(Dialog)
        self.pushBt_update.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.pushBt_update.setObjectName("pushButton_2")
        #########|
        self.pushBt_update = QtWidgets.QPushButton(Dialog)
        self.pushBt_update.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.pushBt_update.setObjectName("pushBt_update") #update button
        #self.pushBt_update.setDisabled(True)


        self.pushBt_update.clicked.connect(self.updateBt_pushed)
        #########################################################
        #########################################################


        self.pushBt_login.clicked.connect(self.loginBt_pushed)
        #########################################################

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # event handler 설치 : 상응하는 버튼에 설치 모듈화 하기 전 테스트로 여기 배치 나중에 다르게 빼도 괜찮음

    def loginBt_pushed(self):  # 로그인 팝업창
        print("Login Btn pressed")
        dinput = ['아이디', '비밀번호']
        # Call the UI and get the inputs
        dialog = login_popup.Dialog(dinput)
        if dialog.exec_() == login_popup.Dialog.Accepted:
            self.profile = dialog.get_output()
            print(self.profile)
            self.label_7.setText(self.profile['sname'] + '님 환영합니다')
            self.pushBt_login.hide()

    def updateBt_pushed(self):
        if (self.profile == -1):
            QMessageBox.information(self, "Error", "로그인이 필요한 기능입니다")
            # print('로그인 하지 않은 상태입니다.')
        else:
            crawl = Crawler()
            crawl.get_major_lecture(self.profile)
            crawl.close()

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
        self.ckBox_grdEtc.setText(_translate("Dialog", "*"))
        self.ckBox_grd1.setText(_translate("Dialog", "1"))
        self.ckBox_grd2.setText(_translate("Dialog", "2"))
        self.ckBox_grd3.setText(_translate("Dialog", "3"))
        self.ckBox_grd4.setText(_translate("Dialog", "4"))

        self.ckBox_major.setText(_translate("Dialog", "전공"))
        self.ckBox_Mbasic.setText(_translate("Dialog", "전공기반"))
        self.ckBox_basis.setText(_translate("Dialog", "기본소양"))

        # 체크 박스 리스너 마냥,, -- def checkBoxState로 처리
        self.ckBox_major.stateChanged.connect(self.checkBoxState)
        self.ckBox_basis.stateChanged.connect(self.checkBoxState)
        self.ckBox_Mbasic.stateChanged.connect(self.checkBoxState)

        self.ckBox_grdEtc.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd1.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd2.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd3.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd4.stateChanged.connect(self.checkBoxState)

        # 슬라이더 리스너
        self.GradeSlider.valueChanged.connect(self.MoveSlider)

        self.comboBox.setItemText(0, _translate("Dialog", "교수명"))
        self.comboBox.setItemText(1, _translate("Dialog", "과목명"))
        self.comboBox.setItemText(2, _translate("Dialog", "과목코드"))
        self.pushBt_search.setText(_translate("Dialog", "검색"))
        self.label_2.setText(_translate("Dialog", "졸업학점/ 이수학점"))
        self.pushBt_login.setText(_translate("Dialog", "로그인"))
        self.label_7.setText(_translate("Dialog", " 학점을 보기 위해서는 로그인이 필요합니다."))
        self.label_7.resize(self.label_7.sizeHint())        # 라벨 내용만큼 자동 리사이징
        self.pushBt_update.setText(_translate("Dialog", "강의\n업데이트"))



