import sqlite3
conn = sqlite3.connect('./Stu.db')
cursor = conn.cursor()
mylist = ['sno','sname' , 'sex','sgrade']
def InsertStu(sno,sname='',sex='',sgrade=''):
    try:
        cursor.execute('INSERT INTO student (sno,sname,sex,sgrade) VALUES (?,?,?,?)',(sno,sname,sex,sgrade))
        conn.commit()
    except:
        print('插入失败！')
def DelStu(sno):
    try:
        cursor.execute('DELETE FROM student WHERE sno=?',(sno,))
        conn.commit()
    except:
        print('删除失败！')
def UpdateStu(sno,sname,sex,sgrade):
    try:
        cursor.execute('UPDATE student SET sname=?,sex=?,sgrade=? WHERE sno=?', (sname,sex,sgrade,sno))
        conn.commit()
    except:
        print('更新失败！')
def SelectStu(sno):
    cursor.execute('SELECT * FROM student WHERE sno like ? ',('%'+sno+'%',))
    values = cursor.fetchall()
    print(mylist)
    for i in values:
        print(i)
    conn.commit()
def Lookstu():
    cursor.execute('SELECT * FROM student')
    values = cursor.fetchall()
    print(mylist)
    for i in values:
        print(i)
    conn.commit()

