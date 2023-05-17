import mysql.connector as sql
conn = sql.connect(host="localhost", user="final", password="2807")
cur = conn.cursor()
# Test connection (this step is optional)
print(conn)
cmd = "CREATE DATABASE week14_db"
cur.execute(cmd)
conn.close()
