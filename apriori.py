from operator import add
from functools import reduce
from collections import Counter
from itertools import combinations


def preprocessing(data):
    """ preprocesses data to be applicable to apriori

    Parameters
    ----------
    data : tbd

    Returns
    ---------
    list of sets
    """
    pass


class Apriori():
    """ Frequent Itemsets using the apriori algorithm

    Parameters
    ----------
    baskets : list of sets

    max_set_size : int, default None
                   determine frequent item sets up to max_set_size items
                   if None, determine alls frequent item sets

    threshold : float >0 and <=1
        minimum threshold for item sets to count as frequent
    """
    def __init__(self, baskets, max_set_size=None, threshold=0.1):
        if baskets == []:
            raise ValueError("baskets must not be an empty list")

        self.baskets = baskets
        self.max_set_size = max_set_size
        self.threshold = threshold

    def compute(self):
        """ Applies the apriori algorithm to baskets
        """
        pass

    def _initialize(self):
        pass

    def _construct(self):
        pass

    def _filter(self):
        pass

    def _construct_and_count(self, baskets, frequent_itemsets, j):
        if j == 1:
            item_counts = reduce(add, map(Counter, self.baskets))
            return item_counts
        if j > 1:
            # for every basket, filter tuples subset of basket
            # double loop through filtered tuples
                # if tuple difference is j-2, unite and count unison
            # if count(unison) = j add tuple to output and increase count
            pass


def baskets_items_counts(baskets):
    """ Constructs the item counts of the items over all baskets

    Parameters
    ----------
    baskets : list of sets
        each basket is a set of items

    Returns
    ----------
    item_counts : Counter object
        each key is a frozenset constructed from all the items in any set of
        baskets
    """
    if baskets == []:
        item_counts = Counter()
    else:
        item_counts = reduce(add,
                             map(Counter,
                                 map(lambda x: {frozenset({key}) for key in x},
                                     baskets
                                     )
                                 )
                             )
    return item_counts


def freq_itemsets_per_basket(basket, freq_itemsets, itemset_size):
    """ Constructs frequent item sets of a basket

    For a given basket coming from the frequent item sets each of size
    itemset_size-1 the frequent item sets of size itemset_size are constructed

    Parameters
    ----------
    basket : set
    freq_itemsets : Counter of frozensets
        contains frequent items, each of length itemset_size-1, as keys and
        their corresponding counts
    itemset_size : size of the frequent items to compute

    Returns:
    ----------
    frequent : Counter of frozensets
        contains the frequent items in basket of size itemset_size as keys.
        The corresponding count is set to 1.

    Raises
    ---------
    ValueError : if itemset_size is less than 2
    """
    if itemset_size < 2:
        raise ValueError("itemset_size needs to be at least 2")
    keys_in_basket = {
        key for key in freq_itemsets.keys() if key.issubset(basket)
        }
    k_combs = Counter(x.union(y) for x, y in combinations(keys_in_basket, 2)
                      if len(x & y) == itemset_size-2 and
                      len(x | y) == itemset_size
                      )
    frequent = Counter(
        key for key, value in k_combs.items() if value ==
        (itemset_size-1)*itemset_size/2
        )
    return frequent
