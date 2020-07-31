from django.test import TestCase

from django.contrib import auth
from .models import *

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = MyUser.objects.create_user('test@dom.com', '1000-12-12', 'pass1234')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass1234')
