import sqlite3
conn = sqlite3.connect('./Stu.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE student (sno varchar(20) PRIMARY KEY, sname varchar(20),sex varchar(20),sgrade varchar(20))')

cursor.close()
conn.commit()
conn.close()