from stock_app.processor import ProcessStockList

stock_list = [
    {"order_id": 123, "stock_name": "ABCD", "quantity": 20, "price": 121, "type": "sell"}
]

processor = ProcessStockList()

processor.getData(stock_list)

processor.getStockList()
