# Handle creation, deletion and editing of events
import re


class EventsClass(object):
   # Handles creation of events
    

    def __init__(self):
        # list to hold events a user creates
        self.events_list = []

    def getOwner(self, user):
        # Returns events belonging to a user
        
        user_events_list = [
            item for item in self.events_list if item['owner'] == user]
        return user_events_list

    def allEvents(self):
        # returns all existing events
        all_events = [
            item for item in self.events_list
        ]
        return all_events

    def createEvent(self, event_name, user, category, location, date):
        # Handles creation of events           
        # Check for special characters
        if re.match("^[a-zA-Z0-9 _]*$", event_name):
            # Get users shopping lists
            my_event = self.getOwner(user)
            # check if name of list already exists
            # for item in my_event:
            #     if list_name == item['name']:
            #         return "Event name already exists."
            events_dict = {
                'name': event_name,
                'owner': user,
                'category': category,
                'location': location,
                'date': date,
            }
            self.events_list.append(events_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.getOwner(user)

    def editEvent(self, edit_name, new_name, user):
        # Handles edits made to event name           
        # editted name and original name
          
        if re.match("^[a-zA-Z0-9 _]*$", edit_name):
            # Get users lists
            my_event = self.getOwner(user)
            for item in my_event:                
                if new_name == item['name']:
                    del item['name']
                    edit_dict = {
                        'name': edit_name,
                    }
                    item.update(edit_dict)                
        else:
            return "No special characters (. , ! space [] )"
        return self.getOwner(user)

    
    def deleteEvent(self, event_name, user):
        # Handles removal of events using list comprehension
          
        # Delete shopping list with name = list_name
        for item in range(len(self.events_list)):
            if self.events_list[item]['name'] == event_name:
                del self.events_list[item]
                break
        # Get users shopping list
        my_events = self.getOwner(user)
        return my_events


    