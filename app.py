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
    username = request.form.get("username")
    password=request.form.get("password")
    
    admin = Admin.query.filter_by(username=username , password=password).first()
    if admin:
        return redirect("/admin")
    
    student= Student.query.filter_by(name = username , password=password).first()
    if student:
        return redirect("/student")
    
    company = Company.query.filter_by(company_name=username , password=password).first()
    if company:    
        if company.approval_status !="approved":
            return "Company not approved by admin yet "
        return redirect("/company")
    
    return "Invalid credentials"

    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=='GET' :
        return render_template("register.html")
    if request.method=='POST' :
        
        role = request.form.get('role')
        name= request.form.get('username')
        email= request.form.get('email')
        password= request.form.get('password')
        
        student_exist = Student.query.filter_by(email=email).first()
        company_exist = Company.query.filter_by(email=email).first()
        if student_exist or company_exist:
            return "Email already registered"
        
        if role == 'student':
            student = Student(
                name=name,
                email=email,
                password=password
            )
            db.session.add(student)
        elif role == 'company':
            company = Company(
                company_name=name,
                email=email,
                password=password
            )
            db.session.add(company)
            
            

        db.session.commit()
        return redirect("/login")
        
        

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
        return render_template("admin.html")
    
@app.route("/student")
def student_dashboard():
    return render_template("student.html")


@app.route("/company")
def company_dashboard():
    return render_template("company.html")


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
    
    
    