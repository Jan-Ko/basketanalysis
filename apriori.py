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

    threshold : real number >= 0 and <=1
        minimum threshold for item sets to count as frequent

    Raises
    ----------
    ValueError : if baskets is an empty list or if threshold is not in the
        interval [0,1]
    """
    def __init__(self, baskets, max_set_size=None, threshold=0.1):
        if baskets == []:
            raise ValueError("baskets must not be an empty list")
        if threshold > 1 or threshold < 0:
            raise ValueError("threshold must be in the range [0,1]")

        self.baskets = baskets
        self.max_set_size = max_set_size
        self.threshold = threshold
        self.baskets_length = len(self.baskets)


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


def filter_frequent(counted_items, threshold):
        """ Filters a counter object according to a threshold

        Parameters
        ----------
        counted_items : Counter of items
        threshold : real number
            items with count > threshold will be kept

        Returns
        ----------
        frequent_items : Counter of items
        """
        frequent_items = Counter(
            {key: value for key, value in counted_items.items()
             if value >= threshold}
            )
        return frequent_items
