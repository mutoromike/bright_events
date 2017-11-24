"""eventdetails.py"""
import re


class EventDetails(object):
    """Handles details of events
    """

    def __init__(self):
        # list to hold items within a shopping list
        self.events_list = []

    def owner_items(self, user, event_name):
        """Returns event details
        """
        user_events = [item for item in self.events_list if item['owner']
                      == user and item['list'] == event_name]
        return user_events