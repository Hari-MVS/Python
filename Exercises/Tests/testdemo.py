import unittest

class Test_demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class method execution')
    def setUp(self):
        print('setup executed')
    def test_hari(self):
        print('test executed')
    def test_venkat(self):
        print('venkat executed')
    def tearDown(self):
        print('teardown executed')
    @classmethod
    def tearDownClass(cls):
        print('teardown class executed')
unittest.main() 

