#Email Varification Using OTP in Flask

from flask import Flask,render_template,request
from flask_mail import Mail,Message
from random import *

app=Flask(__name__, template_folder= "templates")
mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]='kdina715@gmail.com'
app.config['MAIL_PASSWORD']='1998yasodha'                    #you have to give your password of gmail account
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=randint(000000,999999)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify',methods=["POST"])
def verify():
    email=request.form['email']
    msg=Message(subject='OTP',sender='kdina715@gmail.com',recipients=[email])
    msg.body=str(otp)
    mail.send(msg)
    return render_template('verify.html')
@app.route('/validate',methods=['POST'])
def validate():
    user_otp=request.form['otp']
    if otp==int(user_otp):
        return "<h3>Email verification succesfull</h3>"
    return "<h3>Please Try Again</h3>"
if __name__ == '__main__':
    app.run(debug=True)