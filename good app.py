from flask import Flask, request, session, redirect, url_for, jsonify
from markupsafe import escape  # Import escape function to prevent XSS
from flask_wtf.csrf import CSRFProtect  # Import Flask-WTF for CSRF protection
from werkzeug.security import generate_password_hash, check_password_hash  # Use hashed passwords

app = Flask(__name__)
app.secret_key = 'your_secure_random_key'  # Secure secret key for session management
csrf = CSRFProtect(app)  # Initialize CSRF protection

# Vulnerable to XSS (Fixed)
@app.route('/greet')
def greet_user():
    user_name = request.args.get('name')
    return f"<h1>Hello, {escape(user_name)}!</h1>"  # Escape user input to prevent XSS

# Vulnerable to SQL Injection (Fixed)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Fixed: Use parameterized queries to prevent SQL injection
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        session['user'] = username
        return 'Logged in successfully!'
    return 'Invalid credentials!'

# Broken Authentication (Fixed)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f'Welcome, {session["user"]}!'
    return redirect(url_for('home'))  # Redirect to home if not logged in

# Security Misconfiguration: Exposing sensitive data (Fixed)
@app.route('/api/data')
def api_data():
    sensitive_data = {"api_key": "your_secure_api_key", "username": "admin"}
    return jsonify(sensitive_data)  # Never expose sensitive information like passwords

# CSRF Vulnerability (Fixed)
@app.route('/change-password', methods=['POST'])
def change_password():
    # CSRF protection is enabled for all forms with Flask-WTF
    new_password = request.form['password']
    # You should store the new password securely (hashed) in a real application
    return 'Password changed successfully!'

@app.route('/')
def home():
    return '''
        <form action="/change-password" method="POST">
            <input type="text" name="password" placeholder="New Password" required>
            <input type="submit" value="Change Password">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=False)  # Disable debugging in production
