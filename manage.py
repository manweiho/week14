from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector as sql
app = Flask(__name__, template_folder = '/home/ubuntu/templates/')

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_employee():
   return render_template('employee.html')


@app.route('/registration',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         EmpID = request.form['id']
         EmpName = request.form['nm']
         EmpGender = request.form['g']
         EmpPhone = request.form['phone']
         EmpBdate = request.form['date']

         with sql.connect(host="localhost", user="final", password="2807", database="week14_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employee (EmpID,EmpName,EmpGender,EmpPhone,EmpBdate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(EmpID,EmpName,EmpGender,EmpPhone,EmpBdate)
            cur.execute(cmd)

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/information')
def information():
   with sql.connect(host="localhost", user="final", password="2807", database="week14_db") as conn:
   
    cur = conn.cursor()
    cur.execute("select * from employee")
   
    rows = cur.fetchall(); 
   return render_template("information.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
