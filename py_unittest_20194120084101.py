from django.test import TestCase


from py_error_20194120084101 import C20194120084101

class TestModel01(TestCase):

    def test_01(self):
        x = C20194120084101()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20194120084101()
        self.assertIs(x.calc(7,3),21)