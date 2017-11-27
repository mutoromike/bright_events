"""eventdetails.py"""
import re
from app.events import EventsClass


class EventDetails(object):
    # Handles details of events
    

    def __init__(self):
        # A list to add RSVP to events
        self.rsvp_list = []
        self.events_obj = EventsClass()

    def ownerEvents(self, user, event_name):
        # Returns event details
        
        user_events = [item for item in self.rsvp_list if item['owner']
                      == user and item['event'] == event_name]
        return user_events

    def events(self, event_name):
        # returns all existing events
        all_events = [
            item for item in self.events_obj.events_list
        ]
        return all_events

    def addGuest(self, event_name, guest_name, user):
        # Handles adding new guest to an event 
        if re.match("^[a-zA-Z0-9 _]*$", guest_name):
            # Get users items       
            my_events = self.ownerEvents(user, event_name)
            for item in my_events:
                if item['name'] == guest_name:
                    return "You have already RSVP to this event!"
            activity_dict = {
                'name': guest_name,
                'event': event_name,
                'owner': user
            }
            self.rsvp_list.append(activity_dict)
            return self.ownerEvents(user, event_name)
        return "No special characters (. , ! space [] )"

    
