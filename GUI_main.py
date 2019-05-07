from Crawl import Crawler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, Qt, pyqtSlot
import login_popup
import Search_lecture

creditCstate = [False]
gradeCstate = [False, False, False, False, False]  # * 1 2 3 4
typeCstate = [False, False, False]  # 공학전공 전공기반 기본소양


query = "";
callFlag = False

def getquery():
    global query
    query +=";"
    return query

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
         print("Row : %d | Column : %d" % (row, column))  # 선택된 영역 row,col 받아오기

    def cell_dragged(self,row,col):     #drag시 선택된 영역 row, col 받아오기
     #global count
     #global table_x
     #global table_y    table에 대한 return을 따로 주지 않고 search_lecture에 있는 변수를 받아와서 사용
     Search_lecture.table_x.append(row)
     Search_lecture.table_y.append(col)
     print('Start pos : ' + str(Search_lecture.table_x[0])+' , '+str(Search_lecture.table_y[0]))                          #시작 지점
     print('End pos : ' + str(Search_lecture.table_x[len(Search_lecture.table_x)-1])+
           ' , '+str(Search_lecture.table_y[len(Search_lecture.table_y)-1]))  #끝   지점

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

    def checkBoxState(self): #누를 때 마다 실시간으로 반응하기 위함
        # creditName = ["'1'", "'2'", "'3'", "'4'", "'5'"];
        gradeName = ["'*'", "'1'", "'2'", "'3'", "'4'"];
        typeName = ["'공학전공'", "'전공기반'", "'기본소양'"];
        global typeCstate
        global gradeCstate
        global creditCstate
        global query
        global callFlag

        query = "select * from Course where "
        if self.ckBox_major.isChecked():
            typeCstate[0] = True
        else:
            typeCstate[0] = False

        if self.ckBox_Mbasic.isChecked():
            typeCstate[1] = True
        else:
            typeCstate[1] = False

        if self.ckBox_basis.isChecked():
            typeCstate[2] = True
        else:
            typeCstate[2] = False

        orN = sum(typeCstate) - 1
        if(sum(typeCstate)>0):
            query += "("
            for i in range (len(typeCstate)):
                if typeCstate[i]:
                    query += "type = " + typeName[i]
                    if orN > 0:
                        query += ' or '
                        orN -= 1
            query += ")"


        if self.ckBox_grdEtc.isChecked():
            gradeCstate[0] = True
        else:
            gradeCstate[0] = False

        if self.ckBox_grd1.isChecked():
            gradeCstate[1] = True
        else:
            gradeCstate[1] = False

        if self.ckBox_grd2.isChecked():
            gradeCstate[2] = True
        else:
            gradeCstate[2] = False

        if self.ckBox_grd3.isChecked():
            gradeCstate[3] = True
        else:
            gradeCstate[3] = False

        if self.ckBox_grd4.isChecked():
            gradeCstate[4] = True
        else:
            gradeCstate[4] = False

        if(sum(typeCstate)>0 and sum(gradeCstate)>0): #앞에 하나라도 클릭된 게 있고 뒤에도 클릭된 게 있다면
            query += " and "

        orN = sum(gradeCstate) - 1
        if(sum(gradeCstate)>0):
            query += "("
            for i in range (len(gradeCstate)):
                if gradeCstate[i]:
                    query += "year = " + gradeName[i]
                    if orN > 0:
                        query += ' or '
                        orN -= 1
            query += ")"

            if(creditCstate[0]):
                query += self.MoveSlider() # submsg 받아옴

        totalClickSum = sum(gradeCstate) + sum(typeCstate)
        if(totalClickSum == 0 ):
            query = "select * from Course"
            if(creditCstate[0]):
                callflag = True
                self.MoveSlider()


        print(getquery())

        return query

    def MoveSlider(self):
        global query
        global gradeCstate
        global typeCstate
        global creditCstate

        submsg =""
        size = self.GradeSlider.value()
        creditCstate[0] = True;

        if(sum(gradeCstate) + sum(typeCstate)):
            submsg += " and "
            submsg += "credit = " + str(size)
            index = query.rfind("credit")
            if (index > 0): # 앞서 credit 검색이 존재한다면
                temp = query.rsplit("credit", 1)
                query = temp[0]
                query += "credit = " + str(size)
            else: #존재하지 않는다면
                temp = query.rsplit(";", 1)
                query = temp[0]
                query += submsg
        else:
            query = "select * from Course where " + "credit = " + str(size)


        # print(size) return에서 size도 뺀 상황
        #  print(submsg)
        if(callFlag):
            return submsg
        else:
            print(getquery())

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(959, 591)
### Frame 1
        self.frame1 = QtWidgets.QFrame(Dialog) #frame1은 왼쪽의 타임테이블 있는 프레임
        self.frame1.setGeometry(QtCore.QRect(0, 10, 651, 451))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.TimeTable = QtWidgets.QTableWidget(self.frame1) #시간표 테이블
        self.TimeTable.setGeometry(QtCore.QRect(10, 40, 631, 411))
        self.TimeTable.setShowGrid(True)
        self.TimeTable.setGridStyle(QtCore.Qt.SolidLine)
        self.TimeTable.setRowCount(13)
        self.TimeTable.setColumnCount(6)
        self.TimeTable.setObjectName("TimeTable")

        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(5, item)
        # 셀 클릭시 row col 출력
        self.TimeTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.TimeTable.cellClicked.connect(self.cell_clicked)       #단일 cell 선택시 작동하는 함수
        self.TimeTable.cellEntered.connect(self.cell_dragged)       #다수의 cell 선택시 작동하는 삼수


        self.TTableLabel = QtWidgets.QLabel(self.frame1) #TimetableLabel
                 # 레이블은 주로 텍스트 상자를 뜻함, 건드릴일 거의 없음
        self.TTableLabel.setGeometry(QtCore.QRect(30, 0, 501, 41))
        self.TTableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TTableLabel.setObjectName("TTableLabel")

### Frame 2
        self.frame2 = QtWidgets.QFrame(Dialog) #frame2는 오른쪽 과목검색있는곳
        self.frame2.setGeometry(QtCore.QRect(660, 10, 281, 451))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        self.Subjectlist = QtWidgets.QListView(self.frame2) #과목리스트 나오는 상자
        self.Subjectlist.setGeometry(QtCore.QRect(0, 160, 221, 281))
        self.Subjectlist.setObjectName("Subjectlist")

        testsubject = ('새벽', '아침', '점심', '저녁', '밤')
        timeslot = QtGui.QStandardItemModel()
        for f in testsubject:
            timeslot.appendRow(QtGui.QStandardItem(f))
        self.Subjectlist.setModel(timeslot)     #입력받은 데이터값 출력부

        self.SubSearchLabel = QtWidgets.QLabel(self.frame2) #과목검색 레이블
        self.SubSearchLabel.setGeometry(QtCore.QRect(0, 0, 211, 31))
        self.SubSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SubSearchLabel.setObjectName("SubSearchLabel")

        self.CreditLabel = QtWidgets.QLabel(self.frame2) #학점 레이블
        self.CreditLabel.setGeometry(QtCore.QRect(6, 29, 30, 20))
        self.CreditLabel.setObjectName("CreditLabel")

        self.GradeLabel = QtWidgets.QLabel(self.frame2) #학년 레이블
        self.GradeLabel.setGeometry(QtCore.QRect(6, 53, 30, 20))
        self.GradeLabel.setObjectName("GradeLabel")

        self.GubunLabel = QtWidgets.QLabel(self.frame2)  # 구분 레이블
        self.GubunLabel.setGeometry(QtCore.QRect(5, 80, 30, 20))
        self.GubunLabel.setObjectName("GubunLabel")

        self.GradeLayoutWidget = QtWidgets.QWidget(self.frame2) #학년 Layout의 위젯
        self.GradeLayoutWidget.setGeometry(QtCore.QRect(40, 50, 231, 31))
        self.GradeLayoutWidget.setObjectName("GradeLayoutWidget")

        self.GradeLayout = QtWidgets.QHBoxLayout(self.GradeLayoutWidget) #학년Layout 자체(widget과 다른 것임)
        self.GradeLayout.setContentsMargins(0, 0, 0, 0)
        self.GradeLayout.setObjectName("GradeLayout")




        self.ckBox_grdEtc = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 *표
        self.ckBox_grdEtc.setObjectName("ckBox_grdEtc")
        self.GradeLayout.addWidget(self.ckBox_grdEtc)

        self.ckBox_grd1 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 1학년
        self.ckBox_grd1.setObjectName("ckBox_grd1")
        self.GradeLayout.addWidget(self.ckBox_grd1)

        self.ckBox_grd2 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 2학년
        self.ckBox_grd2.setObjectName("ckBox_grd2")
        self.GradeLayout.addWidget(self.ckBox_grd2)

        self.ckBox_grd3 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 3학년
        self.ckBox_grd3.setObjectName("ckBox_grd3")
        self.GradeLayout.addWidget(self.ckBox_grd3)

        self.ckBox_grd4 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 4학년
        self.ckBox_grd4.setObjectName("ckBox_grd4")
        self.GradeLayout.addWidget(self.ckBox_grd4)

        self.GubunLayoutWidget = QtWidgets.QWidget(self.frame2) #구분,즉 전공,전공기반 같은거 체크박스 들어있는 레이아웃
        self.GubunLayoutWidget.setGeometry(QtCore.QRect(40, 75, 231, 31))
        self.GubunLayoutWidget.setObjectName("GubunLayoutWidget")

        self.GubunLayout = QtWidgets.QHBoxLayout(self.GubunLayoutWidget) #구분 레이아웃
        self.GubunLayout.setContentsMargins(0, 0, 0, 0)
        self.GubunLayout.setObjectName("GubunLayout")





        self.ckBox_major = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 전공
        self.ckBox_major.setObjectName("ckBox_major")
        self.GubunLayout.addWidget(self.ckBox_major)

        self.ckBox_Mbasic = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 전공기반
        self.ckBox_Mbasic.setObjectName("ckBox_Mbasic")
        self.GubunLayout.addWidget(self.ckBox_Mbasic)

        self.ckBox_basis = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 기본소양
        self.ckBox_basis.setObjectName("ckBox_basis")
        self.GubunLayout.addWidget(self.ckBox_basis)

        self.GradeSlider = QtWidgets.QSlider(self.frame2) #학점 구분 슬라이더
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

        self.SearchCombo = QtWidgets.QComboBox(self.frame2) # 검색하는 상자 옆에 교수명같은거 있는 combobox
        self.SearchCombo.setGeometry(QtCore.QRect(7, 131, 51, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchCombo.sizePolicy().hasHeightForWidth())
        self.SearchCombo.setSizePolicy(sizePolicy)
        self.SearchCombo.setObjectName("SearchCombo")
        self.SearchCombo.addItem("")
        self.SearchCombo.addItem("")
        self.SearchCombo.addItem("")

        self.SearchTextEdit = QtWidgets.QPlainTextEdit(self.frame2) #검색어 입력할 텍스트 상자
        self.SearchTextEdit.setGeometry(QtCore.QRect(60, 130, 161, 21))
        self.SearchTextEdit.setAcceptDrops(True)
        self.SearchTextEdit.setAutoFillBackground(False)
        self.SearchTextEdit.setLineWidth(1)
        self.SearchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SearchTextEdit.setObjectName("SearchTextEdit")

        self.SearchButton = QtWidgets.QPushButton(self.frame2) #검색하기 버튼
        self.SearchButton.setGeometry(QtCore.QRect(220, 130, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        self.SearchButton.setObjectName("SearchButton")


### Frame 3
        self.frame3 = QtWidgets.QFrame(Dialog) #frame 3은 밑의 학점 및 로그인 기능있는 프레임
        self.frame3.setGeometry(QtCore.QRect(10, 470, 801, 80))
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setLineWidth(1)
        self.frame3.setObjectName("frame3")

        self.GraduateLabel = QtWidgets.QLabel(self.frame3) #졸업학점/이수학점 레이블. 건드릴필요없음
        self.GraduateLabel.setGeometry(QtCore.QRect(20, 0, 771, 21))
        self.GraduateLabel.setObjectName("GraduateLabel")

        self.LoginButton = QtWidgets.QPushButton(self.frame3) #로그인기능 버튼
        self.LoginButton.setGeometry(QtCore.QRect(320, 40, 111, 32))
        self.LoginButton.setObjectName("LoginButton")

        self.NeedLoginLabel = QtWidgets.QLabel(self.frame3) #로그인하라는 레이블. 건드릴필요없음
        self.NeedLoginLabel.setGeometry(QtCore.QRect(260, 20, 231, 21))
        self.NeedLoginLabel.setObjectName("NeedLoginLabel")

        self.UpdateButton = QtWidgets.QPushButton(Dialog) #업데이트 버튼
        self.UpdateButton.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.UpdateButton.setObjectName("UpdateButton")
        self.UpdateButton = QtWidgets.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.UpdateButton.setObjectName("UpdateButton")
        #self.pushBt_update.setDisabled(True)
        self.UpdateButton.clicked.connect(self.updateBt_pushed)
        #########################################################
        #########################################################
        self.LoginButton.clicked.connect(self.loginBt_pushed)
        #########################################################
        self.SearchButton.clicked.connect(self.searchBt_pushed)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# event handler 설치 : 상응하는 버튼에 설치 모듈화 하기 전 테스트로 여기 배치 나중에 다르게 빼도 괜찮음
    def searchBt_pushed(self):  # 검색창 입력
        comboResult = self.SearchCombo.currentText()  # 콤보박스 입력값
        searchResult = self.SearchTextEdit.toPlainText()  # 검색창 입력값
        gubunResult = self.checkBoxState()  # 구분 체크박스 입력값
        creditResult = self.MoveSlider()  # 학점 슬라이더 입력값
        print("SearchButton Pushed\n교과구분 : " + comboResult + " 검색어 : " + searchResult)
        print("구분 checkbox : " + gubunResult)
        print("학점 선택 : " + str(creditResult))

    def loginBt_pushed(self):  # 로그인 팝업창
        print("Login Btn pressed")
        dinput = ['아이디', '비밀번호']
        # Call the UI and get the inputs
        dialog = login_popup.Dialog(dinput)
        if dialog.exec_() == login_popup.Dialog.Accepted:
            self.profile = dialog.get_output()
            print(self.profile)
            self.NeedLoginLabel.setText(self.profile['sname'] + '님 환영합니다')
            self.LoginButton.hide()

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
        item = self.TimeTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "월"))
        item = self.TimeTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "화"))
        item = self.TimeTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "수"))
        item = self.TimeTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "목"))
        item = self.TimeTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "금"))
        item = self.TimeTable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "토"))

        self.TTableLabel.setText(_translate("Dialog", "Time Table"))
        self.SubSearchLabel.setText(_translate("Dialog", "과목검색"))
        self.GubunLabel.setText(_translate("Dialog", "구분"))
        self.GradeLabel.setText(_translate("Dialog", "학년"))
        self.CreditLabel.setText(_translate("Dialog", "학점"))

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

        self.SearchCombo.setItemText(0, _translate("Dialog", "교수명"))
        self.SearchCombo.setItemText(1, _translate("Dialog", "과목명"))
        self.SearchCombo.setItemText(2, _translate("Dialog", "과목코드"))
        self.SearchButton.setText(_translate("Dialog", "검색"))
        self.GraduateLabel.setText(_translate("Dialog", "졸업학점/ 이수학점"))
        self.LoginButton.setText(_translate("Dialog", "로그인"))
        self.NeedLoginLabel.setText(_translate("Dialog", " 학점을 보기 위해서는 로그인이 필요합니다."))
        self.NeedLoginLabel.resize(self.NeedLoginLabel.sizeHint())        # 라벨 내용만큼 자동 리사이징
        self.UpdateButton.setText(_translate("Dialog", "강의\n업데이트"))

        mType = [self.ckBox_major, self.ckBox_basis, self.ckBox_Mbasic]
        mYear = [self.ckBox_grdEtc, self.ckBox_grd1, self.ckBox_grd2, self.ckBox_grd3, self.ckBox_grd4]



