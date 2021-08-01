from stock_app.stock_types.StockBase import StockBase


class Sell(StockBase):
    def format_data(self):
        super().format_data()
        self.output["sell_id"] = self.order_id
        return self.output
