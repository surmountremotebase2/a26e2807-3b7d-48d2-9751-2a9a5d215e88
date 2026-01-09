from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import WSBTop10
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [WSBTop10()]
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
        wsb_top_10_holdings = data[("wsb_top_10",)]
        allocations = {"AAPL": 1}
        if wsb_top_10_holdings:
            alloc_dict = wsb_top_10_holdings[-1]['allocations']
            log(f"Trading: {wsb_top_10_holdings[-1]['allocations']}")
            allocations = alloc_dict
        log(f"allocations:{allocations}")
        return TargetAllocation(allocations)