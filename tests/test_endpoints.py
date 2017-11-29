import unittest
from flask_login import current_user, login_manager
from flask_testing import TestCase
from app import app, user_object, events_obj, eventdetails_obj
from app import views

user_object.registerUser("mike", "mikemutoro@gmail.com", "qw12ER5t", "qw12ER5t")


class BaseTestCase(TestCase):
    ''' A base test case. '''

    # Creating an instance of flask app
    def create_app(self):
        app.config.from_object('config')
        return app


class FlaskTestCase(BaseTestCase):
    # Test that flask was set up correctly
    # Test client is what we use to create a test mocking functionality of a current app
    def test_index(self):
        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    # Test that creating event functionality is protected (login reguired)
    def test_events_is_protected_and_requires_login(self):
        response = self.client.get('/events', follow_redirects=True)
        self.assertTrue(b'Please login' in response.data)


class UserViewsTests(BaseTestCase):
    # Test that login page loads correctly
    def test_login_page_loads_correctly(self):
        response = self.client.get('/', content_type="html/text")
        self.assertTrue(b'Login' in response.data)

    # # Test that the login page behaves correctly given correct credentials
    # def test_correct_login(self):
    #     with self.client:
    #         response = self.client.post('/login', data=dict(username="mike", password="qw12ER5t"))
    #         self.assertIn(b'Successfully logged in, create event!', response.data)
    #         self.assertTrue(current_user.id == 'mike')

#     # Test login behaves correctly given the incorrect credentials
#     def test_incorrect_login(self):
#         response = self.client.post('/', data=dict(username="mike", password="qw12ER5t"),
#                                     follow_redirects=True)
#         self.assertTrue(b'Invalid Password' in response.data)




if __name__ == '__main__':
    unittest.main()