# File to handle testing of guests to an event
import unittest
from app.eventdetails import EventDetails


class TestCasesItems(unittest.TestCase):
    
    # Test for existence of rsvp to an event
    # Test for special character guest names
    # Test for correct rsvp subscription
        

    def setUp(self):
        # Setting up guests class
    
        self.guests_class_obj = EventDetails()

    def tearDown(self):
        # Removing guests class
        
        del self.guests_class_obj

    def test_existing_guest(self):
        # Checking existence of a guest
         
        self.guests_class_obj.rsvp_list = \
            [{'guest': 'mike', 'event': 'Marathon'}, {
                'guest': 'mike', 'event': 'Technology'}]        
        msg = self.guests_class_obj.addGuest("Marathon", "mike")
        self.assertIn('You have already RSVP to this event', msg)

    def test_special_characters_name(self):
        # Check for special characters in guest name
        
        msg = self.guests_class_obj.addGuest(
            "Marathon", "mutoro")
        self.assertIn('Successful RSVP', msg)

    def test_correct_rsvp_subscription(self):
        # Test for correct rsvp subscription
        
        msg = self.guests_class_obj.addGuest(
            "Marathon", "mike")
        self.assertEqual(
            msg, "Successful RSVP")


if __name__ == '__main__':
    unittest.main()
