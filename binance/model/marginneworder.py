class Fill:

    def __init__(self):
        self.price = 0.0
        self.qty = 0.0
        self.commission = 0.0
        self.commissionAsset = ""
        

class MarginNewOrder:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
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
        result = MarginNewOrder()
        result.symbol = json_data.get_string("symbol")
        result.orderId = json_data.get_int("orderId")
        result.orderListId = json_data.get_int("orderListId")
        result.clientOrderId = json_data.get_string("clientOrderId")
        result.transactTime = json_data.get_int("transactTime")
        if json_data.contain_key("price"):
            result.price = json_data.get_float("price")
        if json_data.contain_key("origQty"):
            result.origQty = json_data.get_float("origQty")
        if json_data.contain_key("executedQty"):
            result.executedQty = json_data.get_float("executedQty")
        if json_data.contain_key("cummulativeQuoteQty"):
            result.cummulativeQuoteQty = json_data.get_float("cummulativeQuoteQty")
        if json_data.contain_key("status"):
            result.status = json_data.get_string("status")
        if json_data.contain_key("timeInForce"):
            result.timeInForce = json_data.get_string("timeInForce")
        if json_data.contain_key("type"):
            result.type = json_data.get_string("type")
        if json_data.contain_key("side"):
            result.side = json_data.get_string("side")

        if json_data.contain_key("fills"):
            data_list = json_data.get_array("fills")
            element_list = list()
            for item in data_list.get_items():
                element = Fill()
                element.price = item.get_float("price")
                element.qty = item.get_float("qty")
                element.commission = item.get_float("commission")
                element.commissionAsset = item.get_string("commissionAsset")
                element_list.append(element)
            result.fills = element_list      

        return result