from django.test import TestCase


from py_error_20192021102021 import C20192021102021

class TestModel01(TestCase):

    def test_01(self):
        x = C20192021102021()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20192021102021()
        self.assertIs(x.calc(7,3),21)