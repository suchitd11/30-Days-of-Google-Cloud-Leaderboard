import pandas as pd
import pyrebase

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

try:
    # Read csv file
    df = pd.read_csv('student_authentication.csv')
    # Get the data from the csv file
    data = df.values.tolist()
    # Loop through the data
    for user in data:
        # Create a new user
        auth.create_user_with_email_and_password(user[0], user[1])
        print('User created: ' + user[0])
except Exception as e:
    print(e)
