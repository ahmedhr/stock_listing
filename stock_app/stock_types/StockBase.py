from typing import Dict


class StockBase:
    def __init__(self, stock_data: Dict):
        for key in stock_data:
            setattr(self, key, stock_data[key])
        self.output = dict()

    def format_data(self):
        self.output = {
            "sell_id": None,
            "buy_id": None,
            "name": self.stock_name,
            "quantity": self.quantity,
            "price": self.price
        }
        return self.output

    def print_list(self):
        print(self.output)
