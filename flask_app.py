from flask import Flask, app, render_template, request, session, url_for, redirect
from datetime import timedelta
import pyrebase
import pandas as pd
import os

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(hours=1)

# Set a secret key for your application
app.secret_key = "b'\x89\xfe\x15\x03\xe8\xa4Lv\x7f\x139J'"

# Configure Firebase project
config = {
  "apiKey": "AIzaSyAF-aN_HgcWnIv-xd2Jm1A5UJQklHzBegI",
  "authDomain": "daysofcloud-6a7b4.firebaseapp.com",
  "databaseURL": "https://daysofcloud-6a7b4-default-rtdb.firebaseio.com",
  "projectId": "daysofcloud-6a7b4",
  "storageBucket": "daysofcloud-6a7b4.appspot.com",
  "messagingSenderId": "1011005667946",
  "appId": "1:1011005667946:web:b18f9c8cac13b25c72a813",
  "measurementId": "G-CTJ8CM3S4J"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    if "uname" in session:
        my_csv = os.path.join(THIS_FOLDER, 'leaderboard.csv')
        leaderboard = pd.read_csv(my_csv)
        leaderboard = leaderboard.sort_values(by=['Total'], ascending=False)
        leaderboard = leaderboard.values.tolist()
        # print(leaderboard)
        return render_template("index.html", leaderboard=leaderboard)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST','GET'])
def login():
    if "uname" in session:
        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email, password)
                session.permanent = True
                session['uname'] = email
                return redirect(url_for('index'))
            except:
                return render_template("login.html", unsuccesful="Invalid Credentials")
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('uname', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run()