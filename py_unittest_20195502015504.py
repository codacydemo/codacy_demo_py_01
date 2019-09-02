from django.test import TestCase


from py_error_20195502015504 import C20195502015504

class TestModel01(TestCase):

    def test_01(self):
        x = C20195502015504()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20195502015504()
        self.assertIs(x.calc(7,3),21)