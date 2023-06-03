from django.contrib import auth
from django.test import TestCase
from .models import TyprrrUser

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = TyprrrUser.objects.create_user('abhinav1', 'test@dom.com', 'uareadeaf')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='abhinav1', password='uareadeaf')