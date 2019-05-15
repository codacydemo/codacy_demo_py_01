from django.test import TestCase


from py_error_20195715025739 import C20195715025739

class TestModel01(TestCase):

    def test_01(self):
        x = C20195715025739()
        self.assertIs(x.a,10)


    def test_02(self):
        x = C20195715025739()
        self.assertIs(x.calc(7,3),21)