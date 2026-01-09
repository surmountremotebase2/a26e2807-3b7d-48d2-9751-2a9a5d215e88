from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import WikipediaMostViewedMonth
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [WikipediaMostViewedMonth()]
        self.tickers = []

    @property
    def interval(self):
        return "1day"

    @property
    def assets(self):
        return self.tickers

    @property
    def data(self):
        return self.data_list

    def run(self, data):
        wikipedia_most_viewed_month_holdings = data[("wikipedia_most_viewed_month",)]
        allocations = {"AAPL": 1}
        if wikipedia_most_viewed_month_holdings:
            alloc_dict = wikipedia_most_viewed_month_holdings[-1]['allocations']
            #log(f"Trading: {wikipedia_most_viewed_month_holdings[-1]['allocations']}")
            allocations = alloc_dict
        #log(f"allocations:{allocations}")
        return TargetAllocation(allocations)