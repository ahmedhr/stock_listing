from typing import List

from stock_app.factory import get_stock_obj


class ProcessStockList:
    def __init__(self):
        self.stock_list = list()

    def getData(self, stock_list: List[dict]):
        self.stock_list = stock_list

    def getStockList(self):
        for details in self.stock_list:
            stock_class = get_stock_obj(details["type"])
            stock_obj = stock_class(details)
            stock_obj.format_data()
            stock_obj.print_list()
