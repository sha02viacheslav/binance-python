class Trade:

    def __init__(self):
        self.id = None
        self.price = 0.0
        self.qty = 0.0
        self.quoteQty = 0.0
        self.time = 0
        self.isBuyerMaker = False
        self.isBestMatch = False

    @staticmethod
    def json_parse(json_data):
        trade = Trade()
        trade.id = json_data.get_int("id")
        trade.price = json_data.get_float("price")
        trade.qty = json_data.get_float("qty")
        trade.quoteQty = json_data.get_float("quoteQty")
        trade.time = json_data.get_int("time")
        trade.isBuyerMaker = json_data.get_boolean("isBuyerMaker")
        trade.isBestMatch = json_data.get_boolean("isBestMatch")
        
        return trade