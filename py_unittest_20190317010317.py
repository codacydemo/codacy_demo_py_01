from django.test import TestCase


from py_error_20190317010317 import C20190317010317

class TestModel01(TestCase):

    def test_01(self):
        x = C20190317010317()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20190317010317()
        self.assertIs(x.calc(7,3),21)