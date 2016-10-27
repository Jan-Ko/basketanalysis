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


class apriori():
    """ Frequent Itemsets using the apriori algorithm
    
    Parameters
    ----------
    baskets : list of sets
    
    max_set_size : int, default None
                   determine frequent item sets up to max_set_size items
                   if None, determine alls frequent item sets
        
    s : float >0 and <=1
        minimum threshold for item sets to count as frequent
        
    rules : boolen
            if True return association rules additionally to frequent item sets
        
    confidence : boolean
                 if True compute confidence of association rule. Only viable if rules is True
        
    interest : boolean
               if True compute interest of association rule. Only viable if rules is True
    """
    def __init__(self, baskets, max_set_size = None, s = 0.1, 
                     rules = False, confidence=False, interest=False):
        self.baskets = baskets
        self.max_set_size = max_set_size
        self.s = s
        self.rules = rules
        self.confidence = confidence
        self.interest = interest
        
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
    
    def _construct_and_count(self, j, frequent_tuples):
        if j == 1:
            # count items ind baskets and return
        if j > 1:
            # for every basket, filter tuples subset of basket
            # double loop through filtered tuples
                # if tuple difference is j-2, unite and count unison
            # if count(unison) = j add tuple to output and increase count
    
   #memoization? 
    
