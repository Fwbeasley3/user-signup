from flask import Flask,request,redirect,render_template
import cgi
import os
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')





def isLength(length):
    if len(length) <=2 or len(length) >=21:
       return True
    else:
        return False

def passMatch(p1,p2):
    if p1!=p2:
        return True
    else:
        return False


def valid_email(val):
    valid_email = re.compile("[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+\.[a-z]+")
    if valid_email.match(val):
        return True
    else:
        return False



    

@app.route("/", methods=['POST'])
def validate():
    username=request.form['username']
    password=request.form['password']
    verifyPassword=request.form['verify-password']
    email =request.form['email']

    username_error=""
    password_error=""
    verifyPassword_error=""
    email_error=""


    if  isLength(username)== True:                             #check length(username)
        username_error='Username must be between 3 and 20 characters'
        username=''
    elif " " in username:
        username_error='Username must contain no spaces'
        username =''
    
    if isLength(password)==True:
        password_error='Password must be between 3 and 20 characters'
        password = ''
    elif " " in password:
        password_error='Password must contain no spaces'
        password=''
        
    if passMatch(password,verifyPassword)==True:  
        verifyPassword_error='Passwords do not match'
        verifyPassword = ''
                                                                

        

    
       
 
                               
    
   




    
   



    if not username_error and not password_error and not verifyPassword_error and not email_error:
        username= username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html',username_error=username_error,
         password_error=password_error,
         verifyPassword_error=verifyPassword_error,
         email_error=email_error,
         username=username,
         password=password,
         verifyPassword=verifyPassword,
         email=email)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html',username=username)
        











    



app.run()