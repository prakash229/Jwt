import unittest
from django.test import TestCase
from ..forms import RegistrationForm

class RegistrationFormTest(unittest.TestCase):
  
    def test_registration_form(self):
    # test invalid data
        invalid_data = {
            "username": "user@test.com",
            "password": "secret",
            "confirm": "not secret"
            }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

    # test valid data
        valid_data = {
            "username": "user@test.com",
            "password": "secret",
            "confirm": "secret"
        }
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)