

class SymbolOrderbook:

    def __init__(self):
        self.symbol = ""
        self.bidPrice = 0.0
        self.bidQty = 0.0
        self.askPrice = 0.0
        self.askQty = 0.0

    @staticmethod
    def json_parse(json_data):
        symbol_orderbook = SymbolOrderbook()
        symbol_orderbook.symbol = json_data.get_string("symbol")
        symbol_orderbook.bidPrice = json_data.get_float("bidPrice")
        symbol_orderbook.bidQty = json_data.get_float("bidQty")
        symbol_orderbook.askPrice = json_data.get_float("askPrice")
        symbol_orderbook.askQty = json_data.get_float("askQty")
        return symbol_orderbook