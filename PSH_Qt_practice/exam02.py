import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import QCoreApplication

class Exam(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage('안녕하세요.')

        menu = self.menuBar()               # 메뉴바 생성
        menu_file = menu.addMenu('File')    # 그룹 생성
        menu_edit = menu.addMenu('Edit')    # 그룹 생성
        menu_view = menu.addMenu('View')    # 그룹 생성
        
        file_exit = QAction('Exit', self)   # 메뉴 객체 생성
        file_exit.setShortcut('Ctrl+Q')     # 단축키 지정
        file_exit.setStatusTip('누르면 영원히 빠이빠이')  # 스테이터스바 설명 추가
        file_exit.triggered.connect(QCoreApplication.instance().quit) # triggered connect로 종료 버튼

        new_txt = QAction('텍스트 파일', self)
        new_py = QAction('파이썬 파일', self)

        view_stat = QAction('상태표시줄', self, checkable=True)  # 체크 메뉴 생성
        view_stat.setChecked(True)
        view_stat.triggered.connect(self.tglStat)

        file_new = QMenu('New', self)       # 그룹 속의 메뉴 생성
        file_new.addAction(new_txt)
        file_new.addAction(new_py)

        menu_file.addMenu(file_new)
        menu_file.addAction(file_exit)      # 메뉴에 객체 등록
        menu_view.addAction(view_stat)

        self.resize(450, 400)
        self.show()

    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())