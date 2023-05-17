import mysql.connector as sql
conn = sql.connect(host="localhost", user="final", password="2807", database="week14_db")
cur = conn.cursor()
cmd = "CREATE TABLE employee (\
EmpID INT NOT NULL PRIMARY KEY, \
EmpName VARCHAR(30) NOT NULL,\
EmpGender VARCHAR(30), \
EmpPhone VARCHAR(30), \
EmpBdate DATE)"
cur.execute(cmd)
conn.close()
