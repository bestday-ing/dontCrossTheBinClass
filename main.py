import Crawl
import sys
import GUI

# Staring Functions for Execution
dinput = ['아이디', '비밀번호']
# Call the UI and get the inputs
dialog = GUI.Dialog(dinput)
if dialog.exec_() == GUI.Dialog.Accepted:
    KNU_id, KNU_pwd = dialog.get_output()
    print(KNU_id, KNU_pwd) # 비밀번호 콘솔에 그대로 출력 안되게

User_Profile = Crawl.get_profile(KNU_id, KNU_pwd)  # 통합정보시스템 아이디 비밀번호 입력

if (User_Profile != -1):
    Crawl.get_major_lecture(User_Profile)

Crawl.driver.quit()

# 1. my.knu.ac.kr에서 유저 프로필 가져오기
#KNU_id = input('통합정보시스템 아이디 입력 : ')
#password = input("Password is : ")



# 2. 가져온 프로필을 기반으로 lecture 테이블 구성

# 3. GUI 표시