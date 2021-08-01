from stock_app.stock_types.StockBase import StockBase


class Buy(StockBase):
    def format_data(self):
        super().format_data()
        self.output["buy_id"] = self.order_id
        return self.output
