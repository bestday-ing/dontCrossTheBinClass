import sqlite3

DB_Path = "./Project.db"
con = sqlite3.connect(DB_Path)
DB = con.cursor()
def CreateDataBase() :
    DB.execute('CREATE TABLE IF NOT EXISTS Course(code VARCHAR(15) PRIMARY KEY, type TEXT, \
                year SMALLINT, cname TEXT, credit SMALLINT, pname TEXT, time TEXT, room TEXT, etc TEXT);')
    con.commit()

def INSERT(tuple = []) :
    DB.execute("INSERT OR IGNORE INTO Course values(?, ?, ?, ?, ?, ?, ?, ?, ?);", tuple)
    con.commit()

def SELECT_db():
    for row in DB.execute("SELECT * FROM Course"):
         print(row)
    con.commit()

def DELETE():
    query = 'DELETE FROM Course'
    DB.execute(query)
    con.commit()