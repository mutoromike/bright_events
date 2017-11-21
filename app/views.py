from functools import wraps
from flask import render_template, request, session
from app import app, user_object

# Variable stores user's email
user = None


def authorize(f):
    # Function to authenticate users while accessing other pages
    @wraps(f)
    def check(*args, **kwargs):
        """Function to check login status"""
        if "username" in session:
            return f(*args, **kwargs)
        msg = "Please login"
        return render_template("login.html", resp=msg)
    return check


@app.route('/')
def index():
    # Render index page
    
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # User registeration
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirm-password']

        msg = user_object.registerUser(username, email, password, cpassword)
        if msg == "Successfully registered. You can now login!":
            return render_template("login.html", resp=msg)
        return render_template("register.html", error=msg)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handling logging in

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        msg = user_object.login(username, password)
        if msg == "Successfully logged in, create event!":
            session['username'] = username
            global user
            user = username
            user_lists = event_obj.get_owner(user)
            return render_template('events.html', resp=msg, event=user_lists)
        return render_template('login.html', error=msg)
    return render_template("login.html")





@app.route('/logout')
def logout():
    # Logging out
    session.pop('username', None)
    return render_template("index.html")
