from app.models.event import *



event1 = Event('1 Oct', 'Magic Show', 5, 'Ball Room', 'Mesmerising Magic', True)
event2 = Event('1 Nov', 'Eminem', 500, '02', 'Rap Music', False)
event3 = Event('1 Dec', 'Lana Del Ray', 400, 'SECC', 'Music', False)
events = [event1, event2, event3]


def add_new_event(event):
    events.append(event)

def remove_event(event):
    events.remove(event)