from flask import Flask, request, render_template, send_from_directory
import os
from datetime import datetime
from predict import predict_video
from flask import Flask, render_template, request
import pickle
import pandas as pd
from utils.preprocess import preprocess_input
from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import re
import contextlib
import sqlite3
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from create_database import setup_database
from utils1 import login_required, set_session
from flask import (
    Flask, render_template, 
    request, session, redirect
)

app = Flask(__name__)


database = "users.db"
setup_database(name=database)

app.secret_key = 'xpSm7p5bgJY8rNoBjGWiz5yjxM-NEBlW6SIBI62OkLc='

ADMIN_USERNAME = "Rishi"
ADMIN_PASSWORD = "1234"

@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["user"] = username  # Store user in session
            return redirect("/admin")  # Redirect to admin page

        return render_template("admin_login.html", error="Invalid Credentials")

    return render_template("admin_login.html")



UPLOAD_FOLDER = "uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    if "user" not in session or session["user"] != "Rishi":  # Ensure admin is logged in
        return redirect("/admin_login")

    query = "SELECT username, login_time FROM logins ORDER BY login_time DESC"

    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            login_records = conn.execute(query).fetchall()

    return render_template('admin.html', logins=login_records)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict_page')
def predict_page():
    return render_template('predict.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # Set data to variables
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Query for user
    query = 'SELECT username, password, email FROM users WHERE username = :username'
    
    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            account = conn.execute(query, {'username': username}).fetchone()

    if not account: 
        return render_template('login.html', error='Username does not exist')

    # Verify password
    try:
        ph = PasswordHasher()
        ph.verify(account[1], password)
    except VerifyMismatchError:
        return render_template('login.html', error='Incorrect password')

    # Log login time into `logins` table
    login_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert_query = "INSERT INTO logins (username, login_time) VALUES (:username, :login_time)"
    
    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            conn.execute(insert_query, {'username': username, 'login_time': login_time})

    # Set session
    set_session(username=account[0], email=account[2], remember_me='remember-me' in request.form)

    return redirect('/predict_page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    # Store data to variables 
    password = request.form.get('password')
    confirm_password = request.form.get('confirm-password')
    username = request.form.get('username')
    email = request.form.get('email')

    # Verify data
    if len(password) < 8:
        return render_template('register.html', error='Your password must be 8 or more characters')
    if password != confirm_password:
        return render_template('register.html', error='Passwords do not match')
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return render_template('register.html', error='Username must only be letters and numbers')
    if not 3 < len(username) < 26:
        return render_template('register.html', error='Username must be between 4 and 25 characters')

    query = 'select username from users where username = :username;'
    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            result = conn.execute(query, {'username': username}).fetchone()
    if result:
        return render_template('register.html', error='Username already exists')

    # Create password hash
    pw = PasswordHasher()
    hashed_password = pw.hash(password)

    query = 'insert into users(username, password, email) values (:username, :password, :email);'
    params = {
        'username': username,
        'password': hashed_password,
        'email': email
    }

    with contextlib.closing(sqlite3.connect(database)) as conn:
        with conn:
            result = conn.execute(query, params)

    # We can log the user in right away since no email verification
    set_session( username=username, email=email)
    return redirect('/')

@app.route("/predict_page", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Modify this to return both the result and probability scores
            result, probabilities = predict_video(filepath)  # Ensure predict_video returns both

            return render_template("result.html", filename=file.filename, result=result, probabilities=probabilities)

    return render_template("predict.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
