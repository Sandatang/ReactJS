from flask import Flask,render_template,request,session,url_for,flash,redirect
from mysql.connector import connect
import os
from Query import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yoiusaiudiuaiosdoiasd'


@app.route('/')
@app.route('/home')
def home():
    if 'user' in session:
        return render_template('index.html')
    else: return redirect(url_for('login'))

@app.route('/logout')
def logout():
    app.secret_key = os.urandom(32)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    if 'user' not in session:
        return render_template('login.html')
    else: return redirect(url_for('home'))

@app.route('/validation', methods=['POST'])
def validation():
    
    session.pop('_flashes', None)
    username  = request.form['username']
    password  = request.form['password']

    if username == 'a' and password == 'a':
        
        query = Query('student')
        data = query.getData()

        session['loggedin'] = True
        session['user'] = username
        session['students_data'] = data
        return redirect(url_for('home'))
    else:
        flash("Invalid username and password")
    return redirect(url_for('login'))


@app.route("/insert-data", methods=['POST'])
def insertData():
    session.pop('_flashes', None)
    query = Query('student', 
        idno = request.form['idno'],
        lastname = request.form['lastname'],
        firstname = request.form['firstname'],
        course = request.form['course'],
        level = request.form['level'],
    )       
    data = query.addQuery()

    if data:
        flash("Added Successfully")
        session['students_data'] = query.getData()
    else:
        flash("Data not inserted something occured")
    return redirect(url_for('home'))

@app.route("/deleting/<file>.<extension>", methods=['POST'])
def deleteData(file,extension):
    session.pop('_flashes', None)

    id = request.form['id']
    
    if id:
        query = Query('student', id=id)
        data = query.deleteQuery()

        if data:
            flash("Deleted Successfully")
            session['students_data'] = query.getData()
    else:
        flash("Something was wrong please try again.")
    return redirect(url_for('home',file,a))

if __name__ == "__main__":
    app.run(debug=True)