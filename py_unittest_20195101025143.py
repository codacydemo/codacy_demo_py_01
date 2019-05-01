from django.test import TestCase


from py_error_20195101025143 import C20195101025143

class TestModel01(TestCase):

    def test_01(self):
        x = C20195101025143()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20195101025143()
        self.assertIs(x.calc(7,3),21)