import datetime

from django.test import TestCase
from django.utils import timezone

from py_error_20192829112848 import C20192829112848

class TestModel01(TestCase):

    def test_01(self):
        x = C20192829112848()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20192829112848()
        self.assertIs(x.calc(7,3),21)