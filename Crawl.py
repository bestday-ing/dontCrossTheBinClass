from selenium import webdriver
from selenium.webdriver.support.ui import Select
import DataBase
import platform

class Crawler:
    def __init__(self):
        super().__init__()
        macProDriverPath = '/Users/yubin/ChromeDriver/chromedriver'     # 맥북용 드라이버 경로
        windowDriverPath = 'C:\Python\chromedriver'                     # 윈도우용 드라이버 경로
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--window-size=1280,720")  # 윈도우 사이즈 조절해서 모든 column 로드
        #chrome_option.add_argument("headless")                # 창 없는 크롬 모드
        if(platform.system() == 'Windows'): #platform
         self.driver = webdriver.Chrome(windowDriverPath, chrome_options=chrome_option)  # 윈도우 크롬 드라이버 불러오기
        else:
         self.driver = webdriver.Chrome(macProDriverPath, chrome_options=chrome_option)  # 맥 드라이버 불러오기
        self.driver.implicitly_wait(3)

    # select 태그에서 선택 1. select 클래스 이용
    def select_Search_by_ID(self, id, find):       # id : html id 태그, find : 타겟
        select = Select(self.driver.find_element_by_id(id))
        select.select_by_visible_text(find)

        #select 태그에서 선택 2. xpath와 반복문 이용
    #def select_Search_by_xpath(id, find) :
    #    select = driver.find_element_by_xpath("//select[@id='" + id + "']")
    #    all_options = select.find_elements_by_tag_name('option')
    #    for option in all_options :
    #        if(option.get_attribute('value') == find):

    def get_profile(self, id, pwd):     # 프로필 가져오는 메소드
        self.driver.get('https://my.knu.ac.kr/stpo/comm/support/loginPortal/loginForm.action?redirUrl=%2Fstpo%2Fstpo%2Fmain%2Fmain.action')
        self.driver.find_element_by_name('user.usr_id').send_keys(id)
        self.driver.find_element_by_name('user.passwd').send_keys(pwd)
        self.driver.find_element_by_id('loginBtn').click()
        try:
            self.driver.get('http://my.knu.ac.kr/stpo/stpo/stud/infoMngt/basisMngt/list.action')
            profile = {'sname': '', 'sdept': '', 'smajor': ''}
            profile['sname'] = self.driver.find_element_by_id('kor_nm').get_attribute('value')
            stemp = str(self.driver.find_elements_by_tag_name('td')[8].text).split(' ')
            profile['sdept'] = stemp[2]
            profile['smajor'] = stemp[3]
            return profile
        except:
            alert = self.driver.switch_to_alert()  # alert 창으로 전환
            alert.accept()
            return False

    '''
        url에 접근
        http://sy.knu.ac.kr 사이트는 단순 스크립트 로드해서 보여주는 url 이기 때문에
        html 태그를 로드 하지 못함. 따라서 아래 주소로 직접 연결해야함
    '''
    def get_major_lecture(self, profile):       # 전공 과목 가져오는 메소드
        self.driver.get('http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action')
        self.select_Search_by_ID('mainDiv', '대학')
        self.select_Search_by_ID('sub02', profile['sdept'])
        self.select_Search_by_ID('sub2', profile['smajor'])

        self.driver.find_element_by_id('doSearch').click()

        cTable = self.driver.find_elements_by_tag_name('tr')
        TupleClass = {'code' : 'th4', 'gubun' : 'th2', 'year' : 'th1', 'cname' : 'th5',
                     'credit' : 'th6', 'pname' : 'th9', 'ctime' : 'th10','room' : 'th11' ,'etc' : 'th16'}
        Tuple = list()  # 데이터베이스에 insert 될 튜플

        DataBase.CreateDataBase()
        DataBase.DELETE()
        for Table_row in cTable:
            if(Table_row == cTable[0]):
                continue
            for classname in TupleClass.values():
                Tuple.append(Table_row.find_element_by_class_name(classname).text)
            Tuple[2] = int(Tuple[2])
            Tuple[4] = int(Tuple[4])
            # print(Tuple[6])
            Tuple[6] = self.ParsingT(Tuple[6])
            DataBase.INSERT(Tuple)
            #print(Tuple) # 추가될 튜플 출력
            Tuple.clear()
        DataBase.SELECT_db()

    def close(self):
        self.driver.close()

    def ParsingT(self, TT):
        time_str = ""
        print(TT)
        temp = TT.split('\n')
        print(temp)
        for j in range(len(temp)):  # 배열 길이만큼 j번 돌기
            if (temp[j][0] == '월'):
                col = 0
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '화'):
                col = 1
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '수'):
                col = 2
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '목'):
                col = 3
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '금'):
                col = 4
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '토'):
                col = 5
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '일'):
                col = 6
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
            else:
                col = -999  # 월화수목금토일 이외의 경우 마이너스 가중치 (예외처리용)
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = self.returnROW(k)
                    time = row * 7 + col
                    time_str += str(time) + ','
        time_str = time_str.rstrip(',')  # 마지막에 콤마(,) 하나 떼기
        print(time_str)  # 음수는 0교시 혹은 다른 예외의 경우
        return time_str

    def returnROW(self, single_time):
        row = -1
        if (single_time == '1A'):
            row = 0
        elif (single_time == '1B'):
            row = 1
        elif (single_time == '2A'):
            row = 2
        elif (single_time == '2B'):
            row = 3
        elif (single_time == '3A'):
            row = 4
        elif (single_time == '3B'):
            row = 5
        elif (single_time == '4A'):
            row = 6
        elif (single_time == '4B'):
            row = 7
        elif (single_time == '5A'):
            row = 8
        elif (single_time == '5B'):
            row = 9
        elif (single_time == '6A'):
            row = 10
        elif (single_time == '6B'):
            row = 11
        elif (single_time == '7A'):
            row = 12
        elif (single_time == '7B'):
            row = 13
        elif (single_time == '8A'):
            row = 14
        elif (single_time == '8B'):
            row = 15
        elif (single_time == '9A'):
            row = 16
        elif (single_time == '9B'):
            row = 17
        elif (single_time == '10A'):
            row = 18
        elif (single_time == '10B'):
            row = 19
        elif (single_time == '11A'):
            row = 20
        elif (single_time == '11B'):
            row = 21
        elif (single_time == '12A'):
            row = 22
        elif (single_time == '12B'):
            row = 23
        elif (single_time == '13A'):
            row = 24
        elif (single_time == '13B'):
            row = 25
        elif (single_time == '14A'):
            row = 26
        else:
            row = -100  # 그 이외의 경우 마이너스 가중치(예외처리용)
        return row