import sqlite3

DB_Path = "./Project.db"
con = sqlite3.connect(DB_Path)
DB = con.cursor()
def CreateDataBase() :
    DB.execute('DROP TABLE IF EXISTS Course;')
    DB.execute('DROP TABLE IF EXISTS Time_INDEX;')
    DB.execute('CREATE TABLE IF NOT EXISTS Course(code VARCHAR(15) PRIMARY KEY, type TEXT, \
                year SMALLINT, cname TEXT, credit SMALLINT, pname TEXT, room TEXT, etc TEXT);')
    DB.execute('CREATE TABLE IF NOT EXISTS Time_INDEX(time_id INTEGER PRIMARY KEY AUTOINCREMENT,\
                code VARCHAR(15) REFERENCES Course(code), tindex int);')
    con.commit()

def INSERT(tuple = []) :
    DB.execute("INSERT OR IGNORE INTO Course values(?, ?, ?, ?, ?, ?, ?, ?);", tuple)
    con.commit()

def INSERT_TIME_INDEX(code, ctime = []) :
    for i in range(len(ctime)):
        DB.execute("INSERT OR IGNORE INTO Time_INDEX (code, tindex) values(?, ?);", (code, ctime[i]))
    con.commit()

def SELECT_db():
    for row in DB.execute("SELECT * FROM Course"):
        print(row)
    for row in DB.execute("SELECT * FROM Time_INDEX"):
        print(row)
    con.commit()

def DELETE():
    query = 'DELETE FROM Course'
    DB.execute(query)
    con.commit()

def ParsingT():
    time_str = ""
    for i in DB.execute("SELECT time FROM Course"):     # i: 데이터베이스의 time 속성의 row
        print(i[0])
        temp = i[0].split('\n')
        for j in range(len(temp)):  # 배열 길이만큼 j번 돌기
            if (temp[j][0] == '월'):
                col = 0
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '화'):
                col = 1
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '수'):
                col = 2
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '목'):
                col = 3
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '금'):
                col = 4
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '토'):
                col = 5
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            elif (temp[j][0] == '일'):
                col = 6
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
            else:
                col = -999              # 월화수목금토일 이외의 경우 마이너스 가중치 (예외처리용)
                single = temp[j][1:len(temp[j])]
                single = single.split(',')
                for k in single:
                    row = returnROW(k)
                    time = row*7 + col
                    time_str += str(time) + ','
        time_str = time_str.rstrip(',')     # 마지막에 콤마(,) 하나 떼기
        print(time_str)     # 음수는 0교시 혹은 다른 예외의 경우
        time_str = ""

def returnROW(single_time):
    row = -1
    if(single_time == '1A'):
        row = 0
    elif(single_time == '1B'):
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
        row = -100      # 그 이외의 경우 마이너스 가중치(예외처리용)
    return row