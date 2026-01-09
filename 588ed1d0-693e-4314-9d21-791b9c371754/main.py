from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import CongressSells
from surmount.logging import log
class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [CongressSells()]
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
        congress_sells_holdings = data[("congress_sells",)]
        allocations = {"AAPL": 1}
        if congress_sells_holdings:
            alloc_dict = congress_sells_holdings[-1]['allocations']
            log(f"Trading: {congress_sells_holdings[-1]['allocations']}")
            allocations = alloc_dict
        log(f"allocations:{allocations}")
        return TargetAllocation(allocations)