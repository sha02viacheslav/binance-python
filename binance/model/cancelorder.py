class CancelOrder:

    def __init__(self):
        self.symbol = ""
        self.origClientOrderId = ""
        self.orderId = None
        self.orderListId = None
        self.clientOrderId = ""
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
        order = CancelOrder()
        order.symbol = json_data.get_string("symbol")
        order.origClientOrderId = json_data.get_string("origClientOrderId")
        order.orderId = json_data.get_int("orderId")
        order.orderListId = json_data.get_int("orderListId")
        order.clientOrderId = json_data.get_string("clientOrderId")
        order.price = json_data.get_float("price")
        order.origQty = json_data.get_float("origQty")
        order.executedQty = json_data.get_float("executedQty")
        order.cummulativeQuoteQty = json_data.get_float("cummulativeQuoteQty")
        order.status = json_data.get_string("status")
        order.timeInForce = json_data.get_string("timeInForce")
        order.type = json_data.get_string("type")
        order.side = json_data.get_string("side")

        return order