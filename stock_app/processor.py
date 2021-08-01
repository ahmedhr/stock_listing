from typing import List

from stock_app.factory import get_stock_obj
from stock_app.stock_types.StockBase import StockListing


class ProcessStockList:
    def __init__(self):
        self.stock_listing_obj = StockListing()
        self.stock_list = list()

    def getData(self, stock_list: List[dict]):
        self.stock_list = stock_list

    def getStockList(self):
        for details in self.stock_list:
            # get stock class and create its object
            stock_class = get_stock_obj(details["type"])
            stock_obj = stock_class(details)
            # pass the stock obj to format and print output
            self.stock_listing_obj.format_data(stock_obj)
            self.stock_listing_obj.print_list()
