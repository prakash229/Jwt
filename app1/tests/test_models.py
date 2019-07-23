import unittest
from django.contrib.auth.models import UserManager
from django.test import TestCase
# from app1.models import UserManager

class UserManagerTestCase(TestCase):

    def setUp(self):
        self.author = UserManager(
            username='author@test.com',
            email='author@test.com',
            user_type=UserManager.Author
            )
        self.publisher = UserManager(
            username='publisher@test.com',
            email='publisher@test.com',
            user_type=UserManager.Publisher
            )

    def test_get_authors(self):
        self.assertEqual(UserManager.get_authors(), 1)

    def test_can_write_books(self):
        self.assertTrue(self.author.can_write_books())
        self.assertFalse(self.publisher.can_write_books())
