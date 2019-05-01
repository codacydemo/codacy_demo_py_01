import datetime

from django.test import TestCase
from django.utils import timezone

from py_error_20194001014005 import C20194001014005

class TestModel01(TestCase):

    def test_01(self):
        x = C20194001014005()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20194001014005()
        self.assertIs(x.calc(7,3),21)