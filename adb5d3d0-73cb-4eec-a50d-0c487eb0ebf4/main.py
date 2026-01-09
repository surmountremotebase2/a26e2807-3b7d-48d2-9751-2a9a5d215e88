from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import TopGovernmentContractReceivers
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [TopGovernmentContractReceivers()]
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
        top_government_contract_receivers_holdings = data[("top_government_contract_receivers",)]
        allocations = {"AAPL": 1}
        if top_government_contract_receivers_holdings:
            alloc_dict = top_government_contract_receivers_holdings[-1]['allocations']
            #log(f"Trading: {top_government_contract_receivers_holdings[-1]['allocations']}")
            allocations = alloc_dict
        #log(f"allocations:{allocations}")
        return TargetAllocation(allocations)