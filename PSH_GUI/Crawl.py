from selenium import webdriver
from selenium.webdriver.support.ui import Select
import DataBase
#import GUI
import time

#def driver_init() :
macProDriverPath = '/Users/yubin/ChromeDriver/chromedriver'
windowDriverPath = 'C:\Python\chromedriver'
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--window-size=1280,720")  # 윈도우 사이즈 조절해서 모든 column 로드
driver = webdriver.Chrome( windowDriverPath , chrome_options=chrome_option)  # 크롬 드라이버 불러오기
driver.implicitly_wait(3)

'''
url에 접근
http://sy.knu.ac.kr 사이트는 단순 스크립트 로드해서 보여주는 url 이기 때문에
html 태그를 로드 하지 못함. 따라서 아래 주소로 직접 연결해야함
'''

    # select 태그에서 선택 1. select 클래스 이용
def select_Search_by_ID(id, find) :
    select = Select(driver.find_element_by_id(id))
    select.select_by_visible_text(find)

    #select 태그에서 선택 2. xpath와 반복문 이용
#def select_Search_by_xpath(id, find) :
#    select = driver.find_element_by_xpath("//select[@id='" + id + "']")
#    all_options = select.find_elements_by_tag_name('option')
#    for option in all_options :
#        if(option.get_attribute('value') == find):

def get_profile(id, pwd) :
    driver.get('https://my.knu.ac.kr/stpo/comm/support/loginPortal/loginForm.action?redirUrl=%2Fstpo%2Fstpo%2Fmain%2Fmain.action')
    driver.find_element_by_name('user.usr_id').send_keys(id)
    driver.find_element_by_name('user.passwd').send_keys(pwd)
    driver.find_element_by_id('loginBtn').click()
    try:
        driver.get('http://my.knu.ac.kr/stpo/stpo/stud/infoMngt/basisMngt/list.action')
        profile = {'sname': '', 'sdept': '', 'smajor': ''}
        profile['sname'] = driver.find_element_by_id('kor_nm').get_attribute('value')
        stemp = str(driver.find_elements_by_tag_name('td')[8].text).split(' ')
        profile['sdept'] = stemp[2]
        profile['smajor'] = stemp[3]
        print(profile)
        return profile
    except:
        print('로그인에 실패했습니다.')
        return -1

def get_major_lecture(profile):
    driver.get('http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action')
    select_Search_by_ID('mainDiv', '대학')
    select_Search_by_ID('sub02', profile['sdept'])
    select_Search_by_ID('sub2', profile['smajor'])

    driver.find_element_by_id('doSearch').click()

    cTable = driver.find_elements_by_tag_name('tr')
    TupleClass = {'code' : 'th4', 'gubun' : 'th2', 'year' : 'th1', 'cname' : 'th5',
                 'credit' : 'th6', 'pname' : 'th9', 'ctime' : 'th10','room' : 'th11' ,'etc' : 'th16'}
    Tuple = list()# 데이터베이스에 insert 될 튜플

    DataBase.CreateDataBase()
    DataBase.DELETE()
    for Table_row in cTable:
        if(Table_row == cTable[0]):
            continue
        for classname in TupleClass.values():
            Tuple.append(Table_row.find_element_by_class_name(classname).text)
        Tuple[2] = int(Tuple[2])
        Tuple[4] = int(Tuple[4])
        DataBase.INSERT(Tuple)
        #print(Tuple) # 추가될 튜플 출력
        Tuple.clear()
    DataBase.SELECT_db()

'''
여기서부터 해야할 내용
1. 데이터 저장방식
 - txt 파일
 - sqlite3를 이용한 로컬 데이터베이스 구축
 - 엑셀로 저장
2.
'''



