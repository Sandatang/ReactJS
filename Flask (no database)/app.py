from flask import Flask, url_for, redirect, render_template,request,session,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '%$$Sadasda@)hjh*H@jiS*'

header = ["idno","lastname","firstname","course","level","action"]
students = [
    {
        "idno":"e0001",
        "lastname":"Abad",
        "firstname":"John mark",
        "course":"BSIT",
        "level":"4"
    },
    {
        "idno":"e0002",
        "lastname":"Moncada",
        "firstname":"Shaireen",
        "course":"BSIT",
        "level":"4"
    },
]

@app.route('/')
def home():
    return render_template('index.html', headers = header , data = students)

@app.route('/insert-data', methods=['POST'])
def insertData():
    session.pop('_flashes', None)
    idno = request.form['idno'].strip()
    lastname = request.form['lastname'].title()
    firstname = request.form['firstname'].title()
    course = request.form['course'].upper()
    level = request.form['level']

    # if "" not in list(idno,lastname,firstname,course,level):
    students.append(dict(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level))
    flash("Student added successfully")
    return redirect(url_for('home'))

@app.route('/delete_student', methods=['POST'])
def deleteData():
    session.pop('_flashes', None)
    idno = request.form['idno']
    
    for student in students:
            if idno == student['idno']:
                
                flash('Deleted successfully')
                students.remove(student)
                break

    return redirect(url_for('home'))


@app.route('/edit_data?', methods=['POST'])
def editData():
    session.pop('_flashes', None)
    idno = request.form['idno']
    data_to_edit = []

    for student in students:
        if idno == student['idno']:
            
            data_to_edit.append(student)
            break

    return render_template('edit.html', data= data_to_edit)

@app.route('/edit_proceed', methods=['POST'])
def editInsertData():
    session.pop('_flashes', None)
    
    idno = request.form['idno'].strip()
    lastname = request.form['lastname'].title()
    firstname = request.form['firstname'].title()
    course = request.form['course'].upper()
    level = request.form['level']

    
    for student in students:
        if student['idno'] == idno:
            students.remove(student)
            students.append(dict(idno=idno,lastname=lastname,firstname=firstname,course=course,level=level))
            break
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)