import sqlite3

def ParsingTime(code, Time_ROW):
    if(Time_ROW == ''):
        return -1
    time_arr = list()
    ##print(TT)
    temp = Time_ROW.split(' ')
    #print(temp)
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
    DB.execute("INSERT OR IGNORE INTO Course values(?, ?, ?, ?, ?, ?);", tuple)
    con.commit()

def INSERT_TIME_INDEX(code, ctime = []) :
    for i in range(len(ctime)):
        if(ctime[i] >= 0):
            DB.execute("INSERT OR IGNORE INTO Time_INDEX (code, tindex) values(?, ?);", (code, ctime[i]))
    con.commit()

def SELECT_db():
    for row in DB.execute("SELECT * FROM Time_INDEX WHERE time_id > 1500"):
        print(row)

def CreateDataBase() :
    DB.execute('DROP TABLE IF EXISTS Course;')
    DB.execute('DROP TABLE IF EXISTS Time_INDEX;')
    DB.execute('CREATE TABLE IF NOT EXISTS Course(code VARCHAR(15) PRIMARY KEY, type TEXT, \
                year SMALLINT, cname TEXT, credit SMALLINT, pname TEXT);')
    DB.execute('CREATE TABLE IF NOT EXISTS Time_INDEX(time_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                code VARCHAR(15) REFERENCES Course(code), tindex int);')
    con.commit()
# 데이터베이스 셋업 #
DB_Path = "./Project.db"
con = sqlite3.connect(DB_Path)
DB = con.cursor()
######################
CreateDataBase()

import csv
import pandas as pd

major = open('major_mod.csv','r',encoding='utf-8')
rdr_m = csv.reader(major)
TUPLE = list();
for line in rdr_m:
    if(line[0] == '*'):
        line[0] = line[0].replace('*','0')        # 학년구분 없음: 0으로 casting
    TUPLE.append(line[2])           # 과목코드
    TUPLE.append(line[1])           # 구분
    TUPLE.append(int(line[0]))      # 학년
    TUPLE.append(line[3])           # 과목명
    TUPLE.append(int(line[4]))      # 학점
    TUPLE.append(line[5])           # 담당교수
    print(TUPLE)
    INSERT(TUPLE)                   # Course 테이블에 넣기
    ParsingTime(TUPLE[0], line[6])  # Time_INDEX 테이블 구성
    TUPLE.clear()

SELECT_db()