import os
print("RUNNING FROM:", os.getcwd())
print("APP FILE:", __file__)

from flask import Flask ,render_template,request,redirect,url_for
from model.models import db, Admin, Student, Company, Drive, Application

app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placement.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route('/')
@app.route('/home')
def index():
    return  render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET' :
        return render_template("login.html")
    if request.method=='POST' :
        name=request.form.get('username')
        return render_template("admin.html", username=name)
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET' :
        return render_template("register.html")
    if request.method=='POST' :
        return render_template("home.html")
        

@app.route('/admin', methods=['GET', 'POST'])
def admin():
        return render_template("admin.html")
    

with app.app_context():

    db.create_all()

    if not Admin.query.first():

        admin = Admin(
            username="admin",
            email="dalalgaurav554@gmail.com",
            password="admin123"
        )

        db.session.add(admin)
        db.session.commit()        


if __name__ == '__main__':
    app.run(debug=True)
    
    
    