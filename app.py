import flask
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flaskext.mysql import MySQL
import re
import os
from datetime import date, datetime, timedelta
import smtplib
from email.message import EmailMessage
mysql=MySQL()
#MYSQL_HOST = os.environ.get('MYSQL_HOST')
#MYSQL_USER = os.environ.get('MYSQL_USER')
#MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
#MYSQL_DB = "pyclass"
# UPLOAD_FOLDER = 'C:/Users/MUNA/Desktop/Project/Project'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
import sqlite3
con = sqlite3.connect("employee.db")  
print("Database opened successfully")  
  
con.execute("create table IF NOT EXISTS comment (name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, comment TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  
app = Flask(__name__, template_folder='C:/Users/MUNA/Desktop/FlaskProject/template/')
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'comment'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
# ===================================== Landing Page =====================================
@app.route("/", methods=['GET', 'POST'])

def home():
    if request.method == "POST":
        
        name=request.form['name']
        email=request.form['email']
        comment=request.form['comment']
        with sqlite3.connect("employee.db") as con:  
            cur = con.cursor()  
            cur.execute("INSERT into comment (name, email, comment) values (?,?,?)",(name,email,comment))  
            con.commit()  
        # cur = mysql.get_db().cursor()
        # cur.execute("Insert into comment values('{}','{}','{}')".format(name, email, comment))
        # #cur.execute("INSERT INTO pcl_email_templates (Course_id, Email_Type,Email_Subject,Email_Html,Trigger_1) VALUES (%s, %s, %s, %s,%s)", (Course_id, Email_Type,Email_Subject,Email_Html,Trigger_1))
        # mysql.get_db().commit()
        msg = EmailMessage()
        namemsg = "Name :"+name
        emailmsg = "Email :"+email
        comment = "Comment :"+comment
        msg['Subject'] = 'Comment'
        msg['From'] = "blackconsoletraining@gmail.com"
        msg['To'] = email
        body = "{}\n{}\n{}\n".format(namemsg,emailmsg,comment)
        msg.set_content(body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("blackconsoletraining@gmail.com", "dzsjkqyouhyckxsn")
            smtp.send_message(msg)
        
    return render_template('home.html')

@app.route("/search", methods=['GET', 'POST'])
def search():
    # cur = mysql.get_db().cursor()
    # cur.execute("Select * from employee")
    # data=cur.fetchall()
    # mysql.get_db().commit()
    # if request.method=='POST':
    #     ename=request.form['ename']
    #     cur = mysql.get_db().cursor()
    #     cur.execute("Select id,ename,esal,eaddr from employee where ename='{}'".format(ename))
    #     r=cur.fetchall()
    #     mysql.get_db().commit()
    #     cur.close()
    #     return render_template('search.html',r=r)
    # else:
    #     return render_template('search.html',data=data)
    return render_template('show.html')

app.run(host='127.0.0.1', port=5004, debug=True)


