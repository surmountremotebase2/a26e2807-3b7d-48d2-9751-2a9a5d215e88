from surmount.base_class import Strategy, TargetAllocation, backtest
from surmount.data import HouseNaturalResourcesCommittee
from surmount.logging import log

class TradingStrategy(Strategy):
    def __init__(self):
        self.data_list = [HouseNaturalResourcesCommittee()]
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
        house_natural_resources_committee_holdings = data[("house_natural_resources_committee",)]
        allocations = {"AAPL": 1}
        if house_natural_resources_committee_holdings:
            alloc_dict = house_natural_resources_committee_holdings[-1]['allocations']
            #log(f"Trading: {house_natural_resources_committee_holdings[-1]['allocations']}")
            allocations = alloc_dict
        #log(f"allocations:{allocations}")
        return TargetAllocation(allocations)