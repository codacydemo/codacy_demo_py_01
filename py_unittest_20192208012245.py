from django.test import TestCase


from py_error_20192208012245 import C20192208012245

class TestModel01(TestCase):

    def test_01(self):
        x = C20192208012245()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20192208012245()
        self.assertIs(x.calc(7,3),21)