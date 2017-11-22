from functools import wraps
from flask import render_template, request, session
from app import app, user_object, events_obj

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
            user_events = events_obj.getOwner(user)
            return render_template('events.html', resp=msg, event=user_events)
        return render_template('login.html', error=msg)
    return render_template("login.html")


@app.route('/events', methods=['GET', 'POST'])
@authorize
def Events():
    # Handles events creation
    
    if user == session['username']:
        user_events = events_obj.getOwner(user)
    if request.method == 'POST':
        event_name = request.form['event-name']
        category = request.form['category']
        location = request.form['location']
        date = request.form['date']
        msg = events_obj.createEvent(event_name, user, category, location, date)
        if isinstance(msg, list):
            return render_template('events.html', Events=msg)
        return render_template('events.html', error=msg, Events=user_events)
    return render_template('events.html', Events=user_events)


@app.route('/edit-event', methods=['GET', 'POST'])
@authorize
def save_edits():
    # Editing names of events 
    if user == session['username']:
        user_events = events_obj.getOwner(user=user)
    if request.method == 'POST':
        edit_name = request.form['event_name']
        new_name = request.form['new_name']
        msg = events_obj.editEvent(edit_name, new_name, user)
        if msg == events_obj.events_list:
            response = "Successfully edited event " + new_name
            return render_template('events.html', resp=response, Events=msg)        
        return render_template('events.html', error=msg, Events=user_lists)
    return render_template('events.html')


@app.route('/delete-event', methods=['GET', 'POST'])
@authorize
def delete_event():
    # Deletion of events and their details
    
    if request.method == 'POST':
        del_name = request.form['event_name']
        msg = events_obj.deleteEvent(del_name, user=user)
        # Delete the attendees
        # events_obj.deleted_list_items(del_name)
        response = "Successfuly deleted event " + del_name
        return render_template('events.html', resp=response, Events=msg)



@app.route('/logout')
def logout():
    # Logging out
    session.pop('username', None)
    return render_template("index.html")