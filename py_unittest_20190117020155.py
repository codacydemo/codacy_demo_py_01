from django.test import TestCase


from py_error_20190117020155 import C20190117020155

class TestModel01(TestCase):

    def test_01(self):
        x = C20190117020155()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20190117020155()
        self.assertIs(x.calc(7,3),21)