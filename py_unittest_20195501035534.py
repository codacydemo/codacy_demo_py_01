from django.test import TestCase


from py_error_20195501035534 import C20195501035534

class TestModel01(TestCase):

    def test_01(self):
        x = C20195501035534()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20195501035534()
        self.assertIs(x.calc(7,3),21)