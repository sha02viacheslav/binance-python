class Order:

    def __init__(self):
        self.symbol = ""
        self.orderId = 0.0
        self.clientOrderId = 0.0

    @staticmethod
    def json_parse(json_data):
        result = Balance()
        result.symbol = json_data.get_string("s")
        result.orderId = json_data.get_int("i")
        result.clientOrderId = json_data.get_string("c")
        return result


class ListStatus:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = 0
        self.orderListId = 0
        self.contingencyType = 0
        self.listStatusType = 0
        self.listOrderStatus = 0
        self.listRejectReason = 0
        self.listClientOrderId = 0
        self.transactionTime = 0
        self.orders = list()

    @staticmethod
    def json_parse(json_data):
        result = ListStatus()
        result.eventType = json_data.get_string("e")
        result.eventTime = json_data.get_int("E")
        result.symbol = json_data.get_string("s")
        result.orderListId = json_data.get_int("g")
        result.contingencyType = json_data.get_string("c")
        result.listStatusType = json_data.get_string("l")
        result.listOrderStatus = json_data.get_string("L")
        result.listRejectReason = json_data.get_string("r")
        result.listClientOrderId = json_data.get_string("C")
        result.transactionTime = json_data.get_int("T")
        
        element_list = list()
        data_list = json_data.get_array("O")
        for item in data_list.get_items():
            element = Order.json_parse(item)
            element_list.append(element)
        result.orders = element_list
        return result