"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.conf import settings
#from xmlrpc_webservices import get_id_from_session

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#class LoginTest(TestCase):
#    fixtures = ['test_login']
#    import sys
#    import xmlrpclib
#    
#    def test_returns_token(self):
#        rpc_srv = xmlrpclib.ServerProxy("%s/users/xmlrpc/login/" % settings.HOSTNAME)
#        token = rpc_srv.login('amr', 'admin')
#        assertTrue(get_id_from_session(token))