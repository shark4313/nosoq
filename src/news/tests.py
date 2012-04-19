"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import News
from xmlrpc_webservices import get_news_by_id

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#class GetNewsByIdTest(TestCase):
#    
#    
#    def test_it_returns_one_news_item(self):
        
    