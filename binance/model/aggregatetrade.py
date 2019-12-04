from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class AggregateTrade:

    def __init__(self):
        self.id = None
        self.price = 0.0
        self.qty = 0.0
        self.firstId = None
        self.lastId = None
        self.time = 0
        self.isBuyerMaker = False
        self.isBestMatch = False

    @staticmethod
    def json_parse(json_data):
        trade = AggregateTrade()
        trade.id = json_data.get_int("a")
        trade.price = json_data.get_float("p")
        trade.qty = json_data.get_float("q")
        trade.firstId = json_data.get_int("f")
        trade.lastId = json_data.get_int("l")
        trade.time = convert_cst_in_millisecond_to_utc(json_data.get_int("T"))
        trade.isBuyerMaker = json_data.get_boolean("m")
        trade.isBestMatch = json_data.get_boolean("M")
        
        return trade