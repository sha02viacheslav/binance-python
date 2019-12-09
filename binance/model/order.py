class Order:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
        self.orderListId = None
        self.clientOrderId = ""
        self.price = 0.0
        self.origQty = 0.0
        self.executedQty = 0.0
        self.cummulativeQuoteQty = 0.0
        self.status = None
        self.timeInForce = None
        self.type = None
        self.side = None
        self.stopPrice = 0.0
        self.icebergQty = 0.0
        self.time = 0
        self.updateTime = 0
        self.isWorking = False
        self.origQuoteOrderQty = 0.0

    @staticmethod
    def json_parse(json_data):
        order = Order()
        order.symbol = json_data.get_string("symbol")
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
        order.stopPrice = json_data.get_float("stopPrice")    
        order.icebergQty = json_data.get_float("icebergQty")    
        order.time = json_data.get_int("time")    
        order.updateTime = json_data.get_int("updateTime")    
        order.isWorking = json_data.get_boolean("isWorking")    
        order.origQuoteOrderQty = json_data.get_float("origQuoteOrderQty")    

        return order