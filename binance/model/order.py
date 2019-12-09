class Fill:

    def __init__(self):
        self.price = 0.0
        self.qty = 0.0
        self.commission = 0.0
        self.commissionAsset = ""
        

class Order:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
        self.orderListId = None
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
        self.fills = None

    @staticmethod
    def json_parse(json_data):
        order = Order()
        order.symbol = json_data.get_string("symbol")
        order.orderId = json_data.get_int("orderId")
        order.orderListId = json_data.get_int("orderListId")
        order.clientOrderId = json_data.get_string("clientOrderId")
        order.transactTime = json_data.get_int("transactTime")
        if json_data.contain_key("price"):
            order.price = json_data.get_float("price")
        if json_data.contain_key("origQty"):
            order.origQty = json_data.get_float("origQty")
        if json_data.contain_key("executedQty"):
            order.executedQty = json_data.get_float("executedQty")
        if json_data.contain_key("cummulativeQuoteQty"):
            order.cummulativeQuoteQty = json_data.get_float("cummulativeQuoteQty")
        if json_data.contain_key("status"):
            order.status = json_data.get_string("status")
        if json_data.contain_key("timeInForce"):
            order.timeInForce = json_data.get_string("timeInForce")
        if json_data.contain_key("type"):
            order.type = json_data.get_string("type")
        if json_data.contain_key("side"):
            order.side = json_data.get_string("side")

        if json_data.contain_key("fills"):
            list_array = json_data.get_array("fills")
            fill_list = list()
            for item in list_array.get_items():
                fill = Fill()
                fill.price = item.get_float("price")
                fill.qty = item.get_float("qty")
                fill.commission = item.get_float("commission")
                fill.commissionAsset = item.get_string("commissionAsset")
                fill_list.append(fill)
            order.fills = fill_list      

        return order