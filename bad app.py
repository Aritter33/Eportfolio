# app.py

from flask import Flask, request, session, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'randomkey'  # Insecure secret key for session management

# Vulnerable to XSS
@app.route('/greet')
def greet_user():
    user_name = request.args.get('name')
    return f"<h1>Hello, {user_name}!</h1>"

# Vulnerable to SQL Injection
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vulnerable query construction
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user'] = username
        return 'Logged in successfully!'
    return 'Invalid credentials!'

# Broken Authentication
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f'Welcome, {session["user"]}!'
    return 'Please login to access the dashboard.'

# Security Misconfiguration: Exposing sensitive data
@app.route('/api/data')
def api_data():
    sensitive_data = {"api_key": "123456789", "username": "admin", "password": "password123"}
    return jsonify(sensitive_data)

# CSRF Vulnerability
@app.route('/change-password', methods=['POST'])
def change_password():
    # Vulnerable to CSRF: No CSRF token to verify the source of the request
    new_password = request.form['password']
    return 'Password changed successfully!'

@app.route('/')
def home():
    return '''
        <form action="/change-password" method="POST">
            <input type="text" name="password" placeholder="New Password">
            <input type="submit" value="Change Password">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
