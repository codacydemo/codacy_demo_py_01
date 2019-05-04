from django.test import TestCase


from py_error_20195801035844 import C20195801035844

class TestModel01(TestCase):

    def test_01(self):
        x = C20195801035844()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20195801035844()
        self.assertIs(x.calc(7,3),21)