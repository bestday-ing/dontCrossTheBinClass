from PyQt5.QtGui import QPalette
from Crawl import Crawler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPoint, Qt, pyqtSlot
import login_popup
import Search_lecture       #Table의 좌표를 받아서 검색하는 기능
import DataBase
import threading

creditCstate = [False] #이거 없애고 디폴트 값을 3으로 두는 게 나을 듯
gradeCstate = [False, False, False, False, False]  # * 1 2 3 4
typeCstate = [False, False, False]  # 공학전공 전공기반 기본소양
query = ""
searchClickFlag = False

timeslot = QtGui.QStandardItemModel()



def execQuery(self):
    global creditCstate
    global gradeCstate
    global typeCstate
    global query
    global searchClickFlag

    gradeName = ["'*'", "'1'", "'2'", "'3'", "'4'"]
    typeName = ["'공학전공'", "'전공기반'", "'기본소양'"]

    query = "select * from Course where "
    # type click state check
    orN = sum(typeCstate) - 1
    if (sum(typeCstate) > 0):
        query += "("
        for i in range(len(typeCstate)):
            if typeCstate[i]:
                query += "type = " + typeName[i]
                if orN > 0:
                    query += ' or '
                    orN -= 1
        query += ")"

    if (sum(typeCstate) > 0 and sum(gradeCstate) > 0):  # 앞에 하나라도 클릭된 게 있고 뒤에도 클릭된 게 있다면
        query += " and "
    # grade click state check
    orN = sum(gradeCstate) - 1
    if (sum(gradeCstate) > 0):
        query += "("
        for i in range(len(gradeCstate)):
            if gradeCstate[i]:
                query += "year = " + gradeName[i]
                if orN > 0:
                    query += ' or '
                    orN -= 1
        query += ")"
    # move slider state check
    creditResult = self.GradeSlider.value()  # 학점 슬라이더 입력값
    if (creditResult != 0):
        if (sum(gradeCstate) + sum(typeCstate)):  # 앞서 둘 중에 하나라도 클릭이 되어 있다면
            query += " and "
        # 클릭이 아무것도 안되어 있다면
        query += "credit = " + str(creditResult)

    # search value and state check
    submsg =""
    comboResult = self.SearchCombo.currentText()  # 콤보박스 입력값
    searchResult = self.SearchTextEdit.toPlainText()  # 검색창 입력값

    #입력창에 아무것도 안 쳤을 때 뭔가 예외 처리를 해줘야 할 듯
    print(query)
    if(searchClickFlag): # 클릭했다면
        if(comboResult =="과목코드"): # 과목코드
            submsg += "code = " + "'" + searchResult + "'"
        if (comboResult == "교수명"):
           submsg += "pname = " + "'" + searchResult + "'"
        elif (comboResult == "과목명"):
            submsg += "cname = " + "'" + searchResult + "'"

        index = query.rfind("credit")
        # 앞에 클릭된 게 하나로 있다면 and 붙이고
        if (sum(gradeCstate) + sum(typeCstate)): # 앞서 둘 중에 하나라도 클릭이 되어 있다면
            query += " and "
            query += submsg
        else: #credit이 지금은 항상 클릭되는 상태라서 이렇게 해둠,, 변경 사항있으면 바꾸려고 여기를
            query += " and "
            query += submsg

    print(query)

    self.Subjectlist.setModel(timeslot)  # 입력받은 데이터값 출력부
    timeslot.clear()
    for row in  DataBase.DB.execute(query):
        dataframe =str(row[0]) +'\n'+ str(row[3]+"\n"+row[5])
        timeslot.appendRow(QtGui.QStandardItem(dataframe))
    DataBase.con.commit()

    return query

class Ui_Dialog(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())  # 창 크기 고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 윈도우 레이아웃 제거
        self.profile = -1
        # DBwokrer = threading.Thread(target=execQuery(), args=(self))  # checking 용도
        # DBwokrer.daemon = True  # Daemon Thread
        # DBwokrer.start()


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

    # Key 입력 이벤트
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            temp_x = Search_lecture.table_x
            temp_y = Search_lecture.table_y
            print(temp_x)
            print(temp_y)
        if event.key() == Qt.Key_Escape:        #ESC로 윈도우 종료 이벤트
            self.close()


    def checkBoxState(self): #누를 때 마다 실시간으로 반응하기 위함
        # creditName = ["'1'", "'2'", "'3'", "'4'", "'5'"];
        gradeName = ["'*'", "'1'", "'2'", "'3'", "'4'"]
        typeName = ["'공학전공'", "'전공기반'", "'기본소양'"]
        global typeCstate
        global gradeCstate
        global creditCstate
        global query
        global callFlag

        # query = "select * from Course where "
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

        execQuery(self)

    def MoveSlider(self):
        global query
        global gradeCstate
        global typeCstate
        global creditCstate
        global callFlag
        execQuery(self)




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(959, 591)
        font = QtGui.QFont()
        font.setFamily("휴먼모음T")
        font.setUnderline(False)
        Dialog.setFont(font)
        s = QStyleFactory.create('Fusion')
        Dialog.setStyle(s)

        # palette = QPalette()
        # palette.setColor(QPalette.Base,Qt.)
        # Dialog.setPalette(palette)

### Frame 1
        self.frame1 = QtWidgets.QFrame(Dialog) #frame1은 왼쪽의 타임테이블 있는 프레임
        self.frame1.setGeometry(QtCore.QRect(0, 10, 651, 451))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")


        self.TimeTable = QtWidgets.QTableWidget(self.frame1) #시간표 테이블
        self.TimeTable.setGeometry(QtCore.QRect(15, 40, 631, 411))
        self.TimeTable.setShowGrid(True)
        self.TimeTable.setGridStyle(QtCore.Qt.SolidLine)
        self.TimeTable.setRowCount(26)
        self.TimeTable.setVerticalHeaderLabels(("09:00;09:30;10:00;10:30;11:00;11:30;"
                                                "12:00;12:30;13:00;13:30;14:00;14:30;"
                                                "15:00;15:30;16:00;16:30;17:00;17:30;"
                                                "18:00;18:30;19:00;19:30;20:00;20:30;21:00;21:30").split(";"))
        self.TimeTable.setColumnCount(7)
        self.TimeTable.setObjectName("TimeTable")
        s = QStyleFactory.create('Fusion')
        self.TimeTable.setStyle(s)


        self.TimeTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    #Edit 금지 모드



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
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable.setHorizontalHeaderItem(6, item)
        # 셀 클릭시 row col 출력
        self.TimeTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #self.TimeTable.cellClicked.connect(Search_lecture.get_clicked_pos)       #단일 cell 선택시 작동하는 함수
        #self.TimeTable.cellEntered.connect(Search_lecture.get_dragged_pos)       #다수의 cell 선택시 작동하는 삼수
        self.TimeTable.cellDoubleClicked.connect(self.get_doubleclicked_pos)
        #self.TimeTable.cellPressed.connect(Search_lecture.reset_table)           #수정 필요



        self.TTableLabel = QtWidgets.QLabel(self.frame1) #TimetableLabel
                 # 레이블은 주로 텍스트 상자를 뜻함, 건드릴일 거의 없음
        self.TTableLabel.setGeometry(QtCore.QRect(55, 0, 501, 41))
        self.TTableLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TTableLabel.setObjectName("TTableLabel")
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(16)
        font.setUnderline(False)
        self.TTableLabel.setFont(font)

        self.CateSearchButton = QtWidgets.QPushButton(self.frame1) #카테고리 검색하기 버튼
        self.CateSearchButton.setGeometry(QtCore.QRect(535, 11, 110, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CateSearchButton.sizePolicy().hasHeightForWidth())
        self.CateSearchButton.setSizePolicy(sizePolicy)
        self.CateSearchButton.setObjectName("CateSearchButton")
        s = QStyleFactory.create('Fusion')
        self.CateSearchButton.setStyle(s)

### Frame 2
        self.frame2 = QtWidgets.QFrame(Dialog) #frame2는 오른쪽 과목검색있는곳
        self.frame2.setGeometry(QtCore.QRect(660, 10, 281, 451))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        self.GradeSlider = QtWidgets.QSlider(self.frame2)  # 학점 구분 슬라이더
        self.GradeSlider.setGeometry(QtCore.QRect(41, 28, 221, 22))
        self.GradeSlider.setMaximumSize(QtCore.QSize(221, 16777215))
        self.GradeSlider.setMinimum(0) #1에서 0으로 수정 0은 모든 학점을 말하는것
        self.GradeSlider.setValue(3)
        self.GradeSlider.setMaximum(6)
        self.GradeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.GradeSlider.setInvertedAppearance(False)
        self.GradeSlider.setInvertedControls(False)
        self.GradeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.GradeSlider.setTickInterval(0)
        self.GradeSlider.setObjectName("GradeSlider")
        s = QStyleFactory.create('Fusion')
        self.GradeSlider.setStyle(s)

        self.SliderLabel = QtWidgets.QLabel(self.frame2) #Slider Label
        self.SliderLabel.setGeometry(QtCore.QRect(42, 45, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.SliderLabel.setFont(font)
        self.SliderLabel.setObjectName("SliderLabel")


        self.Subjectlist = QtWidgets.QListView(self.frame2) #과목리스트 나오는 상자
        self.Subjectlist.setGeometry(QtCore.QRect(7, 160, 270, 281))
        self.Subjectlist.setObjectName("Subjectlist")
        self.Subjectlist.setEditTriggers(QAbstractItemView.NoEditTriggers)  #edit 금지 모드
        s = QStyleFactory.create('Fusion')
        self.Subjectlist.setStyle(s)


        self.SubSearchLabel = QtWidgets.QLabel(self.frame2) #과목검색 레이블
        self.SubSearchLabel.setGeometry(QtCore.QRect(35, 0, 211, 31))
        self.SubSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SubSearchLabel.setObjectName("SubSearchLabel")

        self.CreditLabel = QtWidgets.QLabel(self.frame2) #학점 레이블
        self.CreditLabel.setGeometry(QtCore.QRect(8, 29, 30, 20))
        self.CreditLabel.setObjectName("CreditLabel")

        self.GradeLabel = QtWidgets.QLabel(self.frame2) #학년 레이블
        self.GradeLabel.setGeometry(QtCore.QRect(8, 76, 30, 20))
        self.GradeLabel.setObjectName("GradeLabel")

        self.GubunLabel = QtWidgets.QLabel(self.frame2)  # 구분 레이블
        self.GubunLabel.setGeometry(QtCore.QRect(7, 103, 30, 20))
        self.GubunLabel.setObjectName("GubunLabel")

        self.GradeLayoutWidget = QtWidgets.QWidget(self.frame2) #학년 Layout의 위젯
        self.GradeLayoutWidget.setGeometry(QtCore.QRect(40, 71, 231, 31))
        self.GradeLayoutWidget.setObjectName("GradeLayoutWidget")
        s = QStyleFactory.create('Fusion')
        self.GradeLayoutWidget.setStyle(s)

        self.GradeLayout = QtWidgets.QHBoxLayout(self.GradeLayoutWidget) #학년Layout 자체(widget과 다른 것임)
        self.GradeLayout.setContentsMargins(0, 0, 0, 0)
        self.GradeLayout.setObjectName("GradeLayout")




        self.ckBox_grdEtc = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 *표
        self.ckBox_grdEtc.setObjectName("ckBox_grdEtc")
        self.GradeLayout.addWidget(self.ckBox_grdEtc)
        s = QStyleFactory.create('Fusion')
        self.ckBox_grdEtc.setStyle(s)

        self.ckBox_grd1 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 1학년
        self.ckBox_grd1.setObjectName("ckBox_grd1")
        self.GradeLayout.addWidget(self.ckBox_grd1)
        s = QStyleFactory.create('Fusion')
        self.ckBox_grd1.setStyle(s)

        self.ckBox_grd2 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 2학년
        self.ckBox_grd2.setObjectName("ckBox_grd2")
        self.GradeLayout.addWidget(self.ckBox_grd2)
        s = QStyleFactory.create('Fusion')
        self.ckBox_grd2.setStyle(s)

        self.ckBox_grd3 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 3학년
        self.ckBox_grd3.setObjectName("ckBox_grd3")
        self.GradeLayout.addWidget(self.ckBox_grd3)
        s = QStyleFactory.create('Fusion')
        self.ckBox_grd3.setStyle(s)

        self.ckBox_grd4 = QtWidgets.QCheckBox(self.GradeLayoutWidget) #학년 체크박스 4학년
        self.ckBox_grd4.setObjectName("ckBox_grd4")
        self.GradeLayout.addWidget(self.ckBox_grd4)
        s = QStyleFactory.create('Fusion')
        self.ckBox_grd4.setStyle(s)

        self.GubunLayoutWidget = QtWidgets.QWidget(self.frame2) #구분,즉 전공,전공기반 같은거 체크박스 들어있는 레이아웃
        self.GubunLayoutWidget.setGeometry(QtCore.QRect(40, 98, 231, 31))
        self.GubunLayoutWidget.setObjectName("GubunLayoutWidget")
        s = QStyleFactory.create('Fusion')
        self.GubunLayoutWidget.setStyle(s)

        self.GubunLayout = QtWidgets.QHBoxLayout(self.GubunLayoutWidget) #구분 레이아웃
        self.GubunLayout.setContentsMargins(0, 0, 0, 0)
        self.GubunLayout.setObjectName("GubunLayout")





        self.ckBox_major = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 전공
        self.ckBox_major.setObjectName("ckBox_major")
        self.GubunLayout.addWidget(self.ckBox_major)
        s = QStyleFactory.create('Fusion')
        self.ckBox_major.setStyle(s)

        self.ckBox_Mbasic = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 전공기반
        self.ckBox_Mbasic.setObjectName("ckBox_Mbasic")
        self.GubunLayout.addWidget(self.ckBox_Mbasic)
        s = QStyleFactory.create('Fusion')
        self.ckBox_Mbasic.setStyle(s)

        self.ckBox_basis = QtWidgets.QCheckBox(self.GubunLayoutWidget) #구분 - 기본소양
        self.ckBox_basis.setObjectName("ckBox_basis")
        self.GubunLayout.addWidget(self.ckBox_basis)
        s = QStyleFactory.create('Fusion')
        self.ckBox_basis.setStyle(s)

        self.SearchCombo = QtWidgets.QComboBox(self.frame2) # 검색하는 상자 옆에 교수명같은거 있는 combobox
        self.SearchCombo.setGeometry(QtCore.QRect(7, 131, 64, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchCombo.sizePolicy().hasHeightForWidth())
        self.SearchCombo.setSizePolicy(sizePolicy)
        self.SearchCombo.setObjectName("SearchCombo")
        self.SearchCombo.addItem("")
        self.SearchCombo.addItem("")
        self.SearchCombo.addItem("")
        s = QStyleFactory.create('Fusion')
        self.SearchCombo.setStyle(s)

        self.SearchTextEdit = QtWidgets.QPlainTextEdit(self.frame2) #검색어 입력할 텍스트 상자
        self.SearchTextEdit.setGeometry(QtCore.QRect(73, 131, 145, 21))
        self.SearchTextEdit.setAcceptDrops(True)
        self.SearchTextEdit.setAutoFillBackground(False)
        self.SearchTextEdit.setLineWidth(1)
        self.SearchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SearchTextEdit.setObjectName("SearchTextEdit")
        s = QStyleFactory.create('Fusion')
        self.SearchTextEdit.setStyle(s)

        self.SearchButton = QtWidgets.QPushButton(self.frame2) #검색하기 버튼
        self.SearchButton.setGeometry(QtCore.QRect(218, 130, 61, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        self.SearchButton.setObjectName("SearchButton")
        s = QStyleFactory.create('Fusion')
        self.SearchButton.setStyle(s)


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
        s = QStyleFactory.create('Fusion')
        self.LoginButton.setStyle(s)

        self.NeedLoginLabel = QtWidgets.QLabel(self.frame3) #로그인하라는 레이블. 건드릴필요없음
        self.NeedLoginLabel.setGeometry(QtCore.QRect(260, 20, 231, 21))
        self.NeedLoginLabel.setObjectName("NeedLoginLabel")

        self.UpdateButton = QtWidgets.QPushButton(Dialog) #업데이트 버튼
        self.UpdateButton.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.UpdateButton.setObjectName("UpdateButton")
        self.UpdateButton = QtWidgets.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(810, 470, 121, 81))
        self.UpdateButton.setObjectName("UpdateButton")
        s = QStyleFactory.create('Fusion')
        self.UpdateButton.setStyle(s)
        #self.pushBt_update.setDisabled(True)
        self.CateSearchButton.clicked.connect(self.CateSearchBt_pushed)
        self.UpdateButton.clicked.connect(self.updateBt_pushed)
        #########################################################
        #########################################################
        self.LoginButton.clicked.connect(self.loginBt_pushed)
        #########################################################
        self.SearchButton.clicked.connect(self.searchBt_pushed)
        self.Subjectlist.doubleClicked.connect(self.doubleclickList)
        # 슬라이더 리스너
        self.GradeSlider.sliderReleased.connect(self.MoveSlider)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# event handler 설치 : 상응하는 버튼에 설치 모듈화 하기 전 테스트로 여기 배치 나중에 다르게 빼도 괜찮음
    def CateSearchBt_pushed(self):  #카테고리 검색 버튼 클릭
        selValues = self.TimeTable.selectedIndexes() #timetable에 선택된영역 인덱스값 받아옴
        cell = list([idx.row(), idx.column()] for idx in selValues) #객체들 리스트화
        #cell은 2차원 리스트임, 첫번째 선택된 영역의 column값을 받아오려면 cell[0][1]이라고 하면됨
        txt1 = "selected cells ; {0}".format(cell) #스트링으로
        msg = QMessageBox.information(self, 'selectedIndexes()...', txt1)


    def searchBt_pushed(self):  # 검색창 입력
        global searchClickFlag

        searchClickFlag = True
        execQuery(self)
        searchClickFlag = False

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

    def get_doubleclicked_pos(self,row,column):
        reply = QMessageBox.information(self, 'Message', "INDEX\n"+"row - "+str(row)+"\ncolumn - "+str(column), QMessageBox.Yes, QMessageBox.Yes)
        print(reply)

    def doubleclickList(self): #subjectlist 더블클릭 했을시
        currentdata = self.Subjectlist.currentIndex().data()
        datalist = currentdata.split("\n")
        reply = QMessageBox.information(self, 'Message', currentdata+" 을(를) 추가하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == 16384:
            print("YES입력")
            item = QtWidgets.QTableWidgetItem()
            item.setText(datalist[0])
            self.TimeTable.setItem(0,0,item)
        else:
            print("NO입력")

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
        item = self.TimeTable.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "일"))

        self.TTableLabel.setText(_translate("Dialog", "Time Table"))
        self.SubSearchLabel.setText(_translate("Dialog", "과목검색"))
        self.GubunLabel.setText(_translate("Dialog", "구분"))
        self.GradeLabel.setText(_translate("Dialog", "학년"))
        self.CreditLabel.setText(_translate("Dialog", "학점"))
        self.SliderLabel.setText(_translate("Dialog", " *         1          2         3         4          5         6"))

        self.ckBox_grdEtc.setText(_translate("Dialog", "*"))
        self.ckBox_grd1.setText(_translate("Dialog", "1"))
        self.ckBox_grd2.setText(_translate("Dialog", "2"))
        self.ckBox_grd3.setText(_translate("Dialog", "3"))
        self.ckBox_grd4.setText(_translate("Dialog", "4"))

        self.ckBox_major.setText(_translate("Dialog", "전공"))
        self.ckBox_Mbasic.setText(_translate("Dialog", "전공기반"))
        self.ckBox_basis.setText(_translate("Dialog", "기본소양"))

        self.CateSearchButton.setText(_translate("Dialog", "카테고리 검색"))

        # 체크 박스 리스너 마냥,, -- def checkBoxState로 처리
        self.ckBox_major.stateChanged.connect(self.checkBoxState)
        self.ckBox_basis.stateChanged.connect(self.checkBoxState)
        self.ckBox_Mbasic.stateChanged.connect(self.checkBoxState)

        self.ckBox_grdEtc.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd1.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd2.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd3.stateChanged.connect(self.checkBoxState)
        self.ckBox_grd4.stateChanged.connect(self.checkBoxState)



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

        mType[0].setChecked(True)
        mType[1].setChecked(True)
        mType[2].setChecked(True)

        mYear[0].setChecked(True)
        mYear[1].setChecked(True)
        mYear[2].setChecked(True)
        mYear[3].setChecked(True)
        mYear[4].setChecked(True)


