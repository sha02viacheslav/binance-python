

class TradeFee:

    def __init__(self):
        self.symbol = ""
        self.maker = 0.0
        self.taker = 0.0

    @staticmethod
    def json_parse(json_data):
        trade_fee = TradeFee()
        trade_fee.symbol = json_data.get_string("symbol")
        trade_fee.maker = json_data.get_float("maker")
        trade_fee.taker = json_data.get_float("taker")
        return trade_fee