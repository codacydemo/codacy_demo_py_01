from django.test import TestCase


from py_error_20190801040806 import C20190801040806

class TestModel01(TestCase):

    def test_01(self):
        x = C20190801040806()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20190801040806()
        self.assertIs(x.calc(7,3),21)