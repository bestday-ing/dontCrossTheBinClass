import csv
import pandas as pd
from pandas import DataFrame


'''
전공과목 수정
'''


f_major = open('major.csv','r',encoding='utf-8')
out_major = open('major_mod.csv', 'w', encoding='utf-8', newline='')
rdr_m = csv.reader(f_major)
wr_m = csv.writer(out_major)

wr_m.writerow(['학년']+['전공']+['교과코드-구분']+['과목명']+['학점']+['담당교수']+['시간']+['강의실'])
for line in rdr_m:
    if(line[0]== '*'or line[0]=='1'or line[0]=='2' or line[0]=='3'or line[0]=='4'):
     wr_m.writerow((line[0],line[1],line[2],line[3],line[5],line[8],line[9],line[12]))

dataset = pd.read_csv('./major_mod.csv')
print(dataset)      #전체 호출
#print(dataset["과목명"])   #일부분 호출

f_major.close()


'''
교양과목 수정     #수정해야합니다

f_liberal_arts = open('liberalarts.csv','r',encoding='utf-8')
out_liberal_arts = open('lib_mod.csv', 'w', encoding='utf-8', newline='')

rdr_l = csv.reader(f_liberal_arts)
wr_l = csv.writer(out_liberal_arts)

#wr_l.writerow(['전공']+['교과코드-구분']+['과목명']+['학점']+['담당교수']+['시간']+['강의실'])

for line in rdr_l:
    if(line[0]== '*'or line[0]=='1'or line[0]=='2' or line[0]=='3'or line[0]=='4'):
     #wr_l.writerow((line[0],line[1],line[2],line[3],line[5],line[8],line[9],line[12]))
     wr_l.writerow(line)

#dataset2 = pd.read_csv('./lib_mod.csv')
#print(dataset2)

f_liberal_arts.close()
'''