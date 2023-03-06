from flask import Flask, json,redirect,render_template,flash,request
from flask.globals import request, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user
# import os
from flask_mail import Mail
import json

app = Flask(__name__)
app.secret_key="aneesrehmankhan"
local_server=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/login'
db=SQLAlchemy(app)


class login(UserMixin,db.Model): 
    id=db.Column(db.Integer,primary_key=True)
    user=db.Column(db.String(20),unique=True)
    password=db.Column(db.String(20))
class event(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    eventname=db.Column(db.String(100))
    location=db.Column(db.String(50))
    date=db.Column(db.Date)
    time=db.Column(db.Time(5))    
    textarea=db.Column(db.String(500))
    
@app.route("/")
def hello_world():
    return render_template("index.html")
   
# database={'sinha':'123','sonam':'aac','sinhuu':'asdsf'}

# @app.route('/form_login',methods=['POST','GET'])
# def login():
#     name1=request.form['username']
#     pwd=request.form['password']
#     if name1 not in database:
# 	    return render_template('login.html',info='Invalid User')
#     else:
#         if database[name1]!=pwd:
#             return render_template('login.html',info='Invalid Password')
#         else:
# 	         return render_template('home.html',name=name1)


@app.route('/admin',methods=['POST','GET'])
def admin():
 
    if request.method=="POST":
        username=request.form.get('email')
        password=request.form.get('pass')
        if(username=='sonam' and password=='sonam123'):
            # session['user']=username
            flash("login success","info")
            return render_template("admin.html")
        else:
            flash("Invalid Credentials","danger")

    return render_template("login.html")
@app.route('/eventadd',methods=['POST','GET']) 

def eventadd():   
    
      
        if request.method=="POST":
            eventname=request.form.get('eventname')
            location=request.form.get('location')
            date=request.form.get('date')
            time=request.form.get('time')
            textarea=request.form.get('textarea')       
           
            # hcode=hcode.upper()      
           
            
            # flash("Email or srif is already taken","warning")
            # return render_template("event.html")
            db.engine.execute(f"INSERT INTO `event` (`eventname`,`location`,`date`,`time`,`textarea`) VALUES ('{eventname}','{location}','{date}','{time}','{textarea}') ")

            # my mail starts from here if you not need to send mail comment the below line
           
            # mail.send_message('HOTEL MANAGEMENT CENTER',sender='eligiblerock@gmail.com',recipients=[email],body=f"Welcome thanks for choosing us\nYour Login Credentials Are:\n Email Address: {email}\nPassword: {password}\n\nHospital Code {hcode}\n\n Do not share your password\n\n\nThank You..." )

            flash("Data Sent and Inserted Successfully","warning")
            datas=db.engine.execute(f"SELECT `id`,`eventname`,`location`,`date`,`time`,`textarea` FROM `event` order by id desc" )
            return render_template("event.html",datas=datas) 
            

        else:
          flash("Login and try Again","warning")
          return render_template('/admin')      
@app.route("/eventdeatails")
def eventdeatails():
            datas=db.engine.execute(f"SELECT `id`,`eventname`,`location`,`date`,`time`,`textarea` FROM `event` order by id desc" )
            return render_template("event.html",datas=datas)
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

# @login_required
# def eventdeatails():
    # code=current_user.hcode
    # print(code)
         
app.run(debug=True)