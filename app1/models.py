from django.db import models

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    AUTHOR = 1
    PUBLISHER = 2
    USER_TYPES = (
    (AUTHOR, 'Author'),
    (PUBLISHER, 'Publisher'),
    )
    user_type = models.CharField(choices=USER_TYPES)
    no_of_books = models.IntegerField(default=True)

    @classmethod
    def get_authors(cls,):
        return cls.objects.filter(user_type=cls.AUTHOR)

    def can_write_books(self):
        return self.user_type == self.AUTHOR