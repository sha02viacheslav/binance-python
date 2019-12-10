class MarginPriceIndex:

    def __init__(self):
        self.calcTime = 0
        self.price = 0.0
        self.symbol = ""

    @staticmethod
    def json_parse(json_data):
        result = MarginPriceIndex()
        result.calcTime = json_data.get_int("calcTime")
        result.price = json_data.get_float("price")
        result.symbol = json_data.get_string("symbol")
        return result