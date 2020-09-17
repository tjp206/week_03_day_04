from flask import render_template, request
from app import app
from app.models.event import *
from app.models.event_list import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/add-event', methods=['POST'])
def add_event():
    eventDate = request.form['date']
    eventEventName = request.form['event_name']
    eventNumGuests = request.form['num_guests']
    eventRoomLoc = request.form['room_loc']
    eventDesc = request.form['description']
    eventRec = True if 'recurring' in request.form else False
    newEvent = Event(eventDate, eventEventName, eventNumGuests, eventRoomLoc, eventDesc, eventRec)
    add_new_event(newEvent)
    return render_template('index.html', title='Events', events=events)

@app.route('/remove-event', methods=['POST'])
def remove_event_1():
    eventDate = request.form['rem_date']
    eventEventName = request.form['rem_event_name']
    print(eventDate)
    print(eventEventName)
    for event in events:
        if eventEventName == event.event_name and eventDate == event.date:
            remove_event(event)
    return render_template('index.html', title='Events', events=events)





