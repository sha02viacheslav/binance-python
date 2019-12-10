class MarginTrade:

    def __init__(self):
        self.commission = 0.0
        self.commissionAsset = ""
        self.id = None
        self.isBestMatch = False
        self.isBuyer = False
        self.isMaker = False
        self.orderId = None
        self.price = 0.0
        self.qty = 0.0
        self.symbol = ""
        self.time = 0

    @staticmethod
    def json_parse(json_data):
        result = MarginTrade()
        result.commission = json_data.get_float("commission")
        result.commissionAsset = json_data.get_string("commissionAsset")
        result.id = json_data.get_int("id")
        result.isBestMatch = json_data.get_boolean("isBestMatch")
        result.isBuyer = json_data.get_boolean("isBuyer")
        result.isMaker = json_data.get_boolean("isMaker")
        result.orderId = json_data.get_int("orderId")
        result.price = json_data.get_float("price")
        result.qty = json_data.get_float("qty")
        result.symbol = json_data.get_string("symbol")
        result.time = json_data.get_int("time")
        return result
