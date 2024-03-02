from models import User,Session
from flask import *
from sqlalchemy import *
import os


app=Flask(__name__)
app.secret_key='skadwhbhKAcwey'



def verify_login(email,password):
    db_session=Session()
    user_info=db_session.query(User).filter_by(email=email, password=password).first()
    return user_info

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login" , methods=["GET","POST"])
def login():
    if request.method =="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        user_info= verify_login(email,password)
        if user_info:
            return redirect("/")
        else:
            flash("invalid credentials" ,"error")
            return redirect("/login")
    return render_template("login.html")

@app.route("/register" , methods=["GET","POST"])
def register():
    db_session=Session()
    if request.method =="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")
        confirm_password=request.form.get("confirm_password")
        phone=request.form.get("phone")
        
        if password != confirm_password:
            flash("password mismatch")
            return redirect("/register")
        new_user=User(username=username, password=password,email=email,phone=phone)
        db_session.add(new_user)
        db_session.commit()
        db_session.close()
        flash("successfull created an account" , "success")
        return redirect("/login")
        
        
        
    
    return render_template("register.html")





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=int(os.environ.get('PORT', 5000)))