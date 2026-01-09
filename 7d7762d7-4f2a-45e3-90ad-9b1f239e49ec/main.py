from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import WSBMomentum
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [WSBMomentum()]
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
        wsb_momentum_holdings = data[("wsb_momentum",)]
        allocations = {"AAPL": 1}
        if wsb_momentum_holdings:
            alloc_dict = wsb_momentum_holdings[-1]['allocations']
            log(f"Trading: {wsb_momentum_holdings[-1]['allocations']}")
            allocations = alloc_dict
        log(f"allocations:{allocations}")
        return TargetAllocation(allocations)