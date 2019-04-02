import sqlite3
import os
import time

import drill_main
import drill_txt_find

      #what filetype we search for
fPath = ''


# Create database
def createDB():
    conn = sqlite3.connect('text_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT, \
            col_timestamp TEXT \
            )")
        conn.commit()
    conn.close()


# Insert Files
def insertFiles(fPath):
    textString = 'txt'
    conn = sqlite3.connect('text_files.db')
    s = []
    print("The following Files have been added to the text file database: \n")
    with conn:
        cur = conn.cursor()
        for s in os.listdir(fPath):
            if s.endswith(textString):
                allPath = os.path.join(fPath,s)
                cur.execute("INSERT INTO tbl_txt_files(col_filename,col_timestamp) VALUES (?,?)", (s,time.ctime(os.path.getmtime(allPath))))
                print(s)
                print(time.ctime(os.path.getmtime(allPath)))
        conn.commit()
    conn.close()


if __name__ == "__main__":
    createDB()
    insertFiles(fileList,textString)
