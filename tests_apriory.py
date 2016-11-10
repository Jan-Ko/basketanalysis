import unittest
import apriori

class AlgoTestCase(unittest.TestCase):
    def setUp(self):
        self.baskets = [
            {'a','b','c','d'},
            {'a','c','d'}
        ]
