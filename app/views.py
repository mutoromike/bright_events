from functools import wraps
from flask import render_template, request, session, jsonify
from app import app, user_object, events_obj, eventdetails_obj

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


@app.route('/api/v1/auth/register', methods=['GET', 'POST'])
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


@app.route('/api/v1/auth/login', methods=['GET', 'POST'])
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


@app.route('/api/v1/events', methods=['GET', 'POST'])
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


@app.route('/api/v1/edit-event', methods=['GET', 'POST'])
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


@app.route('/api/v1/delete-event', methods=['GET', 'POST'])
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


@app.route('/api/v1/eventdetails/<eventid>', methods=['GET', 'POST'])
@authorize
def eventdetails(eventid):
    my_event = events_obj.getOwner(user)    
    msg = my_event 
    for item in my_event:                
        if eventid == item['name']: 
            msg = my_event
        return render_template('eventdetails.html', Events=msg)
    return render_template('eventdetails.html', error=msg, Events=user_events)

@app.route('/api/v1/userevents', methods=['GET', 'POST'])
def userevents():
    # Displays list of events to users
        
    msg = events_obj.allEvents()
    if isinstance(msg, list):
        return render_template('userevents.html', Events=msg)
    return render_template('userevents.html', error=msg, Events=user_events)


@app.route('/api/v1/<eventid>/rsvp', methods=['GET', 'POST'])
@authorize
def rsvp(eventid):   
    # Adding guests to events (RSVP)
    user = session['username']
    event_name = eventid
    msg1 = eventdetails_obj.addGuest(event_name, user)
    if msg1 == "Successful RSVP":   
        return render_template("rsvp.html", resp=msg1)
    return render_template("rsvp.html", error=msg1)

@app.route('/api/v1/auth/reset-password', methods=['GET', 'POST'])
@authorize
def reset_password():
    #Reseting password
    if request.method == "POST":
        npassword = request.form['npassword']
        cpassword = request.form['cpassword']
        if npassword == cpassword:
            msg = user_object.changePassword(npassword,cpassword)
            return render_template("profile.html", resp=msg)
        else: 
            msg = "The new passwords should match"
            return render_template("profile.html", error=msg)
    return render_template("profile.html")

@app.route('/api/v1/logout')
def logout():
    # Logging out
    session.pop('username', None)
    return render_template("index.html")
