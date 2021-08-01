from abc import ABC
from abc import abstractmethod
from typing import Dict


class StockListing:

    def __init__(self):
        self.stock_data = dict()

    def format_data(self, stock_obj):
        self.stock_data = stock_obj.format_data()

    def print_list(self):
        print(self.stock_data)


class StockBase(ABC):

    def __init__(self, stock_data: Dict):
        for key in stock_data:
            setattr(self, key, stock_data[key])
        self.output = dict()

    @abstractmethod
    def format_data(self):
        self.output = {
            "sell_id": None,
            "buy_id": None,
            "name": self.stock_name,
            "quantity": self.quantity,
            "price": self.price
        }
