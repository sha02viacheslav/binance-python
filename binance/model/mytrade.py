class MyTrade:

    def __init__(self):
        self.symbol = ""
        self.id = None
        self.orderId = None
        self.orderListId = None
        self.price = 0.0
        self.qty = 0.0
        self.quoteQty = 0.0
        self.commission = 0.0
        self.commissionAsset = ""
        self.time = 0
        self.isBuyer = False
        self.isMaker = False
        self.isBestMatch = False

    @staticmethod
    def json_parse(json_data):
        trade = MyTrade()
        trade.symbol = json_data.get_string("symbol")
        trade.id = json_data.get_int("id")
        trade.orderId = json_data.get_int("orderId")
        trade.orderListId = json_data.get_int("orderListId")
        trade.price = json_data.get_float("price")
        trade.qty = json_data.get_float("qty")
        trade.quoteQty = json_data.get_float("quoteQty")
        trade.commission = json_data.get_float("commission")
        trade.commissionAsset = json_data.get_string("commissionAsset")
        trade.time = json_data.get_int("time")
        trade.isBuyer = json_data.get_boolean("isBuyer")
        trade.isMaker = json_data.get_boolean("isMaker")
        trade.isBestMatch = json_data.get_boolean("isBestMatch")
        
        return trade