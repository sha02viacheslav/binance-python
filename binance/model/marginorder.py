class MarginOrder:

    def __init__(self):
        self.clientOrderId = ""
        self.cummulativeQuoteQty = 0.0
        self.executedQty = 0.0
        self.icebergQty = 0.0
        self.isWorking = False
        self.orderId = None
        self.origQty = 0.0
        self.price = 0.0
        self.side = ""
        self.status = ""
        self.stopPrice = 0.0
        self.symbol = ""
        self.time = 0
        self.timeInForce = ""
        self.type = ""
        self.updateTime = 0

    @staticmethod
    def json_parse(json_data):
        result = MarginOrder()
        result.clientOrderId = json_data.get_string("clientOrderId")
        result.cummulativeQuoteQty = json_data.get_float("cummulativeQuoteQty")
        result.executedQty = json_data.get_float("executedQty")
        result.icebergQty = json_data.get_float("icebergQty")
        result.isWorking = json_data.get_boolean("isWorking")
        result.orderId = json_data.get_int("orderId")
        result.origQty = json_data.get_float("origQty")
        result.price = json_data.get_float("price")
        result.side = json_data.get_string("side") 
        result.status = json_data.get_string("status")
        result.stopPrice = json_data.get_float("stopPrice")
        result.symbol = json_data.get_string("symbol")
        result.time = json_data.get_int("time")
        result.timeInForce = json_data.get_string("timeInForce")
        result.type = json_data.get_string("type")
        result.updateTime = json_data.get_int("updateTime")
        return result