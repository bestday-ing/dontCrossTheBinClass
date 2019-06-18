import csv
import pandas as pd
from pandas import DataFrame


'''
전공과목 수정
'''
# column 이름은 ['학년']['전공']['교과코드-구분']['과목명']['학점']['담당교수']['시간']['강의실']로 설정
# []안의 이름 변경시 구분되는 col 이름 변경
# dataset은 csv파일 , 단위로 읽어서 저장되어 있습니다.
# .drop등 명령어로 특정부분 삭제 가능


f_major = open('computer.csv','r',encoding='utf-8')                            #Input 전공 파일 이름
out_major = open('major_mod.csv', 'w', encoding='utf-8' ,newline='')        #Output 전공 파일 이름
rdr_m = csv.reader(f_major)
wr_m = csv.writer(out_major)

#wr_m.writerow(['학년']+['전공']+['교과코드-구분']+['과목명']+['학점']+['담당교수']+['시간'])

for line in rdr_m:
    print(line)
    if(line[0]== '*'or line[0]=='1'or line[0]=='2' or line[0]=='3'or line[0]=='4'):
        line[2] = line[2].replace('-','')
        wr_m.writerow((line[0],line[1],line[2],line[3],line[5],line[8],line[9]))

dataset = pd.read_csv('./major_mod.csv')
#print(dataset)      #전체 호출
#print(dataset["과목명"])   #일부분 호출

f_major.close()


'''
교양과목 수정     #구현했수다
'''


count = 0
f_liberal_arts = open('lib.csv','r',encoding='utf-8')                           #Input 교양 파일 이름
out_liberal_arts = open('lib_mod.csv', 'w', encoding='utf-8', newline='')      #Output 교양 파일 이름

rdr_l = csv.reader(f_liberal_arts)
wr_l = csv.writer(out_liberal_arts)

wr_l.writerow(['학년']+['전공']+['교과코드-구분']+['과목명']+['학점']+['담당교수']+['시간'])#+['강좌관리과'])

for line in rdr_l:
    if(not line[0] and not line[1] and line[2]):
        line[0]='*'
        line[1]='교양'
        line[2] = line[2].replace('-','')
        wr_l.writerow((line[0],line[1],line[2],line[3],line[4],line[8],line[9]))

#dataset2 = pd.read_csv('./lib_mod.csv',sep =',')
#print(dataset2)

f_liberal_arts.close()
