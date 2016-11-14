import unittest
import apriori
from collections import Counter


class BasketsToItemsTestCase(unittest.TestCase):
    """ Test cases fot the basktes_items_counts function
    """
    def setUp(self):
        self.baskets = [
            {'a', 'b', 'c', 'd'},
            {'a', 'c', 'd'}
        ]
        self.counts = Counter({
                        frozenset({'a'}): 2,
                        frozenset({'b'}): 1,
                        frozenset({'c'}): 2,
                        frozenset({'d'}): 2
                        })

    def test_baskets_items_counts(self):
        """ Tests if the for regular baskets output is as expected
        """
        expected = self.counts
        self.assertEqual(apriori.baskets_items_counts(self.baskets), expected)

    def test_baskets_items_counts_empty_list(self):
        """ Tests empty list edge cases
        """
        expected = Counter()
        self.assertEqual(apriori.baskets_items_counts([]), expected)
        self.assertEqual(apriori.baskets_items_counts([{}, {}]), expected)


class CombFreqItemsOfBasketTestCase(unittest.TestCase):
    """ Test cases for the construction of frequent items for a basket
    """

    def setUp(self):
        self.basket = {'a', 'b', 'c', 'd'}
        self.freq_items_edge_case = Counter()
        self.freq_items_1item = Counter({frozenset({'a'}): 1})
        self.freq_items_2items_ct1 = Counter({frozenset({'a'}): 1,
                                              frozenset({'b'}): 1
                                              })
        self.freq_items_2items_ct2 = Counter({frozenset({'a'}): 2,
                                              frozenset({'b'}): 2
                                              })
        self.freq_items_2items_1inbasket = Counter({frozenset({'a'}): 1,
                                                    frozenset({'e'}): 1
                                                    })
        self.freq_items_3items_2inbasket = Counter({frozenset({'a'}): 1,
                                                    frozenset({'b'}): 1,
                                                    frozenset({'e'}): 1
                                                    })
        self.freq_items_all_single_items = Counter({frozenset({'a'}): 1,
                                                    frozenset({'b'}): 1,
                                                    frozenset({'c'}): 1,
                                                    frozenset({'d'}): 1
                                                    })
        self.freq_items_3pairs = Counter({frozenset({'a', 'b'}): 1,
                                          frozenset({'a', 'c'}): 1,
                                          frozenset({'b', 'c'}): 1
                                          })
        self.freq_items_5_pairs = Counter({frozenset({'a', 'b'}): 1,
                                           frozenset({'a', 'c'}): 1,
                                           frozenset({'b', 'c'}): 1,
                                           frozenset({'b', 'd'}): 1,
                                           frozenset({'c', 'd'}): 1
                                           })
        self.freq_items_4triples = Counter({frozenset({'a', 'b', 'c'}): 1,
                                            frozenset({'a', 'b', 'd'}): 1,
                                            frozenset({'a', 'c', 'd'}): 1,
                                            frozenset({'b', 'c', 'd'}): 1
                                            })

    def test_k_not_in_range(self):
        """ Verify that desired itemset sizes less than two raise a ValueError
        """
        with self.assertRaises(ValueError):
            for itemset_size in range(-1, 2):
                apriori.freq_itemsets_per_basket(self.basket,
                                                 self.freq_items_2items_ct1,
                                                 itemset_size)

    def test_no_frequent_items_input(self):
        """Test Case for an empty set of frequent items
        """
        expected = Counter()
        self.assertEqual(
            apriori.freq_itemsets_per_basket(self.basket,
                                             self.freq_items_edge_case, 2
                                             ), expected)

    def test_single_frequent_item_input(self):
        """ Verifies that single frequent itemsets return empty Counters
        """
        expected = Counter()
        self.assertEqual(
            apriori.freq_itemsets_per_basket(self.basket,
                                             self.freq_items_1item, 2
                                             ), expected)

    def test_frequent_items_of_size1_input(self):
        """ Verfies correct output when constructing pairs
        """
        exptected = Counter({frozenset({'a', 'b'}): 1})
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_2items_ct1,
                2
                ),
            exptected
            )
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_2items_ct2,
                2
                ),
            exptected
            )
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_3items_2inbasket,
                2
                ),
            exptected
            )
        expected = Counter()
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_2items_1inbasket,
                2
                ),
            expected
            )
        expected = Counter({
            frozenset({'a', 'b'}): 1, frozenset({'a', 'c'}): 1,
            frozenset({'a', 'd'}): 1, frozenset({'b', 'c'}): 1,
            frozenset({'b', 'd'}): 1, frozenset({'c', 'd'}): 1
        })
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_all_single_items,
                2
                ),
            expected
            )

    def test_frequent_pairs_input(self):
        """ Verify that frequent triples are constructed correclty from pairs
        """
        expected = Counter({frozenset({'a', 'b', 'c'}): 1})
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_3pairs,
                3
            ),
            expected
            )
        expected = Counter({frozenset({'a', 'b', 'c'}): 1,
                            frozenset({'b', 'c', 'd'}): 1})
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_5_pairs,
                3
            ),
            expected
            )

    def test_frequent_triples_input(self):
        """ verify that four tuples are constructed correctly from triples
        """
        expected = Counter({frozenset({'a', 'b', 'c', 'd'}): 1})
        self.assertEqual(
            apriori.freq_itemsets_per_basket(
                self.basket,
                self.freq_items_4triples,
                4
            ),
            expected
            )


class AprioriInstantiaionTestCase(unittest.TestCase):
    """ Testcases for initialization of the apriori class
    """
    def test_regular_case(self):
        """ standard positive case
        """
        baskets = [{'a', 'b'},
                   {'a'}]
        max_set_size = 2
        threshold = 0.5
        cls = apriori.Apriori(
            baskets=baskets, max_set_size=max_set_size, threshold=threshold
            )
        self.assertEqual(baskets, cls.baskets)
        self.assertEqual(max_set_size, max_set_size)
        self.assertEqual(threshold, threshold)

    def test_empty_basket_case(self):
        """ Ensure ValueError when passing empty baskets
        """
        baskets = []
        with self.assertRaises(ValueError):
            apriori.Apriori(baskets)

    def test_threshold(self):
        """ Ensures that threshold is in the desired range
        """
        def setUp(self):
            self.threshs_neg = [-1, -0.5, 1.5]
            self.threshs_pos = [0, 0.5, 1]
            self.baskets = [{'a'}]

        def test_threshold(self):
            for thresh in self.threshs_pos:
                apr = apriori.Apriori(self.baskets, threshold=thresh)
                self.assertEqual(apr.threshold, thresh)
                self.assertEqual(apr.bbaskets, self.baskets)

            for thresh in self.threshs_neg:
                with self.self.assertRaises(ValueError):
                    apriori.Apriori(self.baskets, thresh)


class FilterFrequentItemTestCase(unittest.TestCase):
    """ Provides tests for filtering frequent items according to a threshold
    """
    def setUp(self):
        self.frequent_standard = Counter({frozenset({'b'}): 0,
                                          frozenset({'e'}): 2})
        self.frequent_empty = Counter()

    def test_filter_frequent_standard_case(self):
        threshs = [-1, 0, 1, 3]
        expected = [self.frequent_standard,
                    self.frequent_standard,
                    Counter({frozenset({'e'}): 2}),
                    Counter()]
        for thresh, exp in zip(threshs, expected):
            self.assertEqual(exp,
                             apriori.filter_frequent(self.frequent_standard,
                                                     thresh)
                             )

    def test_frequent_empty_case(self):
        thresh = 2
        expected = Counter()
        self.assertEqual(expected,
                         apriori.filter_frequent(self.frequent_empty, thresh)
                         )
