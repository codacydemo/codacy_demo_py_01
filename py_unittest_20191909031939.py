from django.test import TestCase


from py_error_20191909031939 import C20191909031939

class TestModel01(TestCase):

    def test_01(self):
        x = C20191909031939()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20191909031939()
        self.assertIs(x.calc(7,3),21)