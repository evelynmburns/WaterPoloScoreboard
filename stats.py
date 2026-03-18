class Stats:
    """
    Collects and maintains counters for various game events.

    This class initializes a set of predefined statistic categories to zero
    and provides a dictionary-based storage for tracking them.

    Attributes
    ----------
    stat : dict
        A dictionary where keys are event names (str) and values are 
        their respective counts (int). 
        Tracked events include: 'exclusion', 'goal', 'block', 'turnover', 
        'shot on goal', 'sprint', 'penalty', 'sub in', 'sub out'.
    """
    def __init__(self):
        # List of all stats that are valid and tracked
        stat_keys = [
            'exclusion', 'goal', 'block', 'turnover', 'shot on goal',
            'sprint', 'penalty', 'sub in', 'sub out'
        ]
        self.stat = {}

        # initialise all stats
        for key in stat_keys:
            self.stat[key] = 0
