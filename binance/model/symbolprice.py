

class SymbolPrice:

    def __init__(self):
        self.symbol = ""
        self.price = 0.0

    @staticmethod
    def json_parse(json_data):
        symbol_price = SymbolPrice()
        symbol_price.symbol = json_data.get_string("symbol")
        symbol_price.price = json_data.get_float("price")
        return symbol_price