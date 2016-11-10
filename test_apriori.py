import unittest
import apriori
from collections import Counter

class BasketsToItemsTestCase(unittest.TestCase):
    """ Test cases fot the basktes_items_counts function
    """
    def setUp(self):
        self.baskets = [
            {'a','b','c','d'},
            {'a','c','d'}
        ]
        self.counts = Counter({
                        frozenset({'a'}):2,
                        frozenset({'b'}):1,
                        frozenset({'c'}):2,
                        frozenset({'d'}):2
                        })

    def test_baskets_items_counts(self):
        """ Tests if the for regular baskets output is as expected
        """
        expected = self.counts
        self.assertEqual(apriori.baskets_items_counts(self.baskets), self.counts)

    def test_baskets_items_counts_empty_list(self):
        """ Tests the empty list edge case
        """
        expected = self.counts
        self.assertEqual(apriori.baskets_items_counts([]), Counter())
