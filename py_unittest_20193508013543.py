from django.test import TestCase


from py_error_20193508013543 import C20193508013543

class TestModel01(TestCase):

    def test_01(self):
        x = C20193508013543()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20193508013543()
        self.assertIs(x.calc(7,3),21)