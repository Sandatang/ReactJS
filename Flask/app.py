from flask import Flask,render_template,request,session,url_for,flash,redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yoiusaiudiuaiosdoiasd'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validation', methods=['POST'])
def validation():
    
    session.pop('_flashes', None)
    username = request.form['username']
    password = request.form['password']

    if username == 'a' and password == 'a':
        return redirect(url_for('home'))
    else:
        flash("Invalid username and password")
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)