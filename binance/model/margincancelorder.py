class MarginCancelOrder:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
        self.origClientOrderId = ""
        self.clientOrderId = ""
        self.transactTime = 0
        self.price = None
        self.origQty = None
        self.executedQty = None
        self.cummulativeQuoteQty = None
        self.status = None
        self.timeInForce = None
        self.type = None
        self.side = None

    @staticmethod
    def json_parse(json_data):
        result = MarginCancelOrder()
        result.symbol = json_data.get_string("symbol")
        result.orderId = json_data.get_int("orderId")
        result.origClientOrderId = json_data.get_string("origClientOrderId")
        result.clientOrderId = json_data.get_string("clientOrderId")
        result.transactTime = json_data.get_int("transactTime")
        result.price = json_data.get_float("price")
        result.origQty = json_data.get_float("origQty")
        result.executedQty = json_data.get_float("executedQty")
        result.cummulativeQuoteQty = json_data.get_float("cummulativeQuoteQty")
        result.status = json_data.get_string("status")
        result.timeInForce = json_data.get_string("timeInForce")
        result.type = json_data.get_string("type")
        result.side = json_data.get_string("side")

        return result