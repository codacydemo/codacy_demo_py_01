from django.test import TestCase


from py_error_20193023043056 import C20193023043056

class TestModel01(TestCase):

    def test_01(self):
        x = C20193023043056()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20193023043056()
        self.assertIs(x.calc(7,3),21)