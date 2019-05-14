from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sqlite3
import platform

def ParsingTime(code, Time_ROW):
    if(Time_ROW == ''):
        return -1
    time_arr = list()
    ##print(TT)
    temp = Time_ROW.split('\n')
    print(temp)
    for j in range(len(temp)):  # 배열 길이만큼 j번 돌기
        if (temp[j][0] == '월'):
            col = 0
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '화'):
            col = 1
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '수'):
            col = 2
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '목'):
            col = 3
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '금'):
            col = 4
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '토'):
            col = 5
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        elif (temp[j][0] == '일'):
            col = 6
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
        else:
            col = -999  # 월화수목금토일 이외의 경우 마이너스 가중치 (예외처리용)
            single = temp[j][1:len(temp[j])]
            single = single.split(',')
            for k in single:
                row = returnROW(k)
                time = row * 7 + col
                time_arr.append(time)
    #time_str = time_str.rstrip(',')  # 마지막에 콤마(,) 하나 떼기
    #print(time_arr)  # 음수는 0교시 혹은 다른 예외의 경우
    #print(code)
    INSERT_TIME_INDEX(code, time_arr)
    return
def returnROW(single_time):
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

def INSERT(tuple = []) :
    DB.execute("INSERT OR IGNORE INTO Course values(?, ?, ?, ?, ?, ?, ?, ?);", tuple)
    con.commit()

def INSERT_TIME_INDEX(code, ctime = []) :
    for i in range(len(ctime)):
        if(ctime[i] >= 0):
            DB.execute("INSERT OR IGNORE INTO Time_INDEX (code, tindex) values(?, ?);", (code, ctime[i]))
    con.commit()

def select_Search_by_ID(id, find):  # id : html id 태그, find : 타겟
    select = Select(driver.find_element_by_id(id))
    select.select_by_visible_text(find)

def SELECT_db():
    for row in DB.execute("SELECT * FROM Course"):
        print(row)
# 크롬 드라이버 및 데이터베이스 셋업 #
windowDriverPath = 'C:/Python/chromedriver'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--window-size=1280,720")  # 윈도우 사이즈 조절해서 모든 column 로드
#chrome_option.add_argument("headless")                # 창 없는 크롬 모드
if(platform.system() == 'Windows'): #platform
    driver = webdriver.Chrome(windowDriverPath, options=chrome_option)  # 윈도우 크롬 드라이버 불러오기
    driver.implicitly_wait(3)
DB_Path = "./Project.db"
con = sqlite3.connect(DB_Path)
DB = con.cursor()
#######################################

def crawled(dept,major):
    driver.get('http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action')
    select_Search_by_ID('mainDiv', '대학')
    select_Search_by_ID('sub02', dept)
    select_Search_by_ID('sub2', major)
    driver.find_element_by_id('doSearch').click()


    cTable = driver.find_elements_by_tag_name('tr')
    TupleClass = {'code' : 'th4', 'gubun' : 'th2', 'year' : 'th1', 'cname' : 'th5',
                 'credit' : 'th6', 'pname' : 'th9', 'room' : 'th11' ,'etc' : 'th16'}
    Tuple = list()  # 데이터베이스에 insert 될 튜플

    for Table_row in cTable:
        if(Table_row == cTable[0]):
            continue
        for classname in TupleClass.values():
            Tuple.append(Table_row.find_element_by_class_name(classname).text)
        if(Tuple[2] == '*'):
            Tuple[2] = 0
        Tuple[2] = int(Tuple[2])
        Tuple[4] = int(Tuple[4])
        #print('Tuple 넣기 이전')
        INSERT(Tuple)
        # print(Tuple[6]))
        #Time_ROW = null
        ParsingTime(Tuple[0], Table_row.find_element_by_class_name('th10').text)

        Tuple.clear()

crawled('IT대학', '전자공학부 모바일공학전공')
crawled('IT대학', '컴퓨터학부 글로벌소프트웨어융합전공')
crawled('IT대학', '핀테크전공')

SELECT_db()
driver.close()