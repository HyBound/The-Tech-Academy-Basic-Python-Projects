import sqlite3

textString = 'txt'      #what filetype we search for
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


# Create database
def createDB():
    conn = sqlite3.connect('test.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files_and_such( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT \
            )")
        conn.commit()
    conn.close()


# Insert Files
def insertFiles(fileList,textString):
    conn = sqlite3.connect('test.db')
    s = []
    
    with conn:
        cur = conn.cursor()
        for s in fileList:
            if s.endswith(textString):
                cur.execute("INSERT INTO tbl_files_and_such(col_filename) VALUES (?)", (s,))
                print(s)
        conn.commit()
    conn.close()


if __name__ == "__main__":
    createDB()
    insertFiles(fileList,textString)
