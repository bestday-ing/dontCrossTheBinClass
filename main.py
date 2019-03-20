import Crawl
import sys
#import GUI

print(sys.argv)
#gui = GUI()

# 1. my.knu.ac.kr에서 유저 프로필 가져오기
KNU_id = input('통합정보시스템 아이디 입력 : ')
password = input("Password is : ")


User_Profile = Crawl.get_profile(KNU_id, password) # 통합정보시스템 아이디 비밀번호 입력
# 2. 가져온 프로필을 기반으로 lecture 테이블 구성
Crawl.get_major_lecture(User_Profile)

# 3. GUI 표시