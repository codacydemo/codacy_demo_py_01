from django.test import TestCase


from py_error_20193602033641 import C20193602033641

class TestModel01(TestCase):

    def test_01(self):
        x = C20193602033641()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20193602033641()
        self.assertIs(x.calc(7,3),21)