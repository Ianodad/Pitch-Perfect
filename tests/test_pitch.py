import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db


class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_joe = User(
            username='jack', password='password', email='xyz@gmail.com')
        self.new_pitch = Pitch(title="Test", pitch=' This is a test')

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.title, "Test")
        self.assertEquals(self.new_pitch.pitch, 'This is test')
        self.assertEquals(self.new_pitch.user, self.user_joe)
