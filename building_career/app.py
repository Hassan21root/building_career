from flask import Flask ,render_template,jsonify,request,abort,redirect
import mysql.connector

app = Flask(__name__)



conn = mysql.connector.connect(host="localhost", user="root", password="brocode", database="jobs_for_flask")
mycursor = conn.cursor()


def load_jobs_from_db():
    sql_query = "SELECT * FROM jobs"
    mycursor.execute(sql_query)
    Result = mycursor.fetchall()
    return Result



def load_job_from_db(id):
    job_id=id
    sql_query = "SELECT * FROM jobs where id =%s"
    name=(job_id,)
    mycursor.execute(sql_query,name)
    Result = mycursor.fetchall()
    if len(Result)==0:
        return None
    return Result



def load_jobs_to_db(id,data):
    query = "insert into application(JID,FULL_NAME,Email,Linkedin_URL,Education,Work_Experience) values (%s,%s,%s,%s,%s,%s);"
    values = (id,data['full_name'], data['email'], data['linked'],data['Education'],data['work-experience'])
    mycursor.execute(query, values)
    conn.commit()


def load_courses_from_db():
    sql_query = "SELECT * FROM courses"
    mycursor.execute(sql_query)
    Result = mycursor.fetchall()
    return Result


def load_events_from_db():
    sql_query = "SELECT * FROM events_for_site"
    mycursor.execute(sql_query)
    Result = mycursor.fetchall()
    return Result

def insert_user(email,username,password):
    query = "insert into users values (%s,%s,%s);"
    values = (username,password,email)
    mycursor.execute(query, values)
    conn.commit()




def check_user(username,password):
    user=(username,)
    query = "select password from users where user=%s"
    mycursor.execute(query,user)
    Result = mycursor.fetchall()
    conn.commit()
    try:
        if Result[0][0] == password:
            return True
        else:
            return False
    except(IndexError):
        abort(401)



@app.route("/")
def hello_world1():
    AllJobs=load_jobs_from_db()
    return render_template('home_before_login.html',arg=AllJobs,Employee='Building')


@app.route("/logedin")
def hello_world2():
    AllJobs=load_jobs_from_db()
    return render_template('home_after_login.html',arg=AllJobs,Employee='Building')

@app.route("/logedin/api/jobs")
def list_jobs():
    AllJobs=load_jobs_from_db()
    return jsonify(AllJobs)

@app.route("/logedin/api/jobs/<id>")
def show_job_json(id):
    job=load_job_from_db(id)
    return jsonify(job)


@app.route("/logedin/jobs/<id>/apply",methods=['post'])
def apply_to_job(id):
    data=request.form
    test=load_job_from_db(id)
    load_jobs_to_db(id,data)
    return render_template('application_submit.html',Application=data,Employee='Building',job=test)



@app.route("/logedin/jobs/<id>")
def show_job(id):
    test=load_job_from_db(id)
    if not test :
        return "Not Found" , 404 
    return render_template('jobPage.html',job=test,Employee='Building')


@app.route("/logedin/courses")
def show_courses():
    Allcourses=load_courses_from_db()
    return render_template('courses.html',arg=Allcourses,Employee='Building')


@app.route("/logedin/events")
def show_events():
    Allevents=load_events_from_db()
    return render_template('events.html',arg=Allevents,Employee='Building')

@app.route("/login")
def Login():    
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def my_form_post():
    username = request.form['username']
    password = request.form['password']
    check = check_user(username,password)
    if check :
        return redirect('/logedin')
        #return "<h1 style='color: green;'>Found</h1>" , 200
    else:
        #return "<h1 style='color: red;'>Not Found</h1>" , 404
        abort(401)


@app.route("/signup")
def signup():    
    return render_template('sign_up.html')




@app.route('/signup', methods=['POST'])
def my_form_post2():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    insert_user(email,username,password)
    return redirect('/logedin')




if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
