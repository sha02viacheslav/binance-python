class Order:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
        self.clientOrderId = ""


class Oco:

    def __init__(self):
        self.orderListId = None
        self.contingencyType = None
        self.listStatusType = None
        self.listOrderStatus = None
        self.listClientOrderId = None
        self.transactionTime = 0
        self.symbol = ""
        self.orders = list()
        self.orderReports = list()

    @staticmethod
    def json_parse(json_data):
        oco = Oco()
        oco.orderListId = json_data.get_int("orderListId")
        oco.contingencyType = json_data.get_string("contingencyType")
        oco.listStatusType = json_data.get_string("listStatusType")
        oco.listOrderStatus = json_data.get_string("listOrderStatus")
        oco.listClientOrderId = json_data.get_string("listClientOrderId")
        oco.transactionTime = json_data.get_int("transactionTime")
        oco.symbol = json_data.get_string("symbol")
    
        list_array = json_data.get_array("orders")
        order_list = list()
        for item in list_array.get_items():
            order = Order()
            order.symbol = item.get_string("symbol")
            order.orderId = item.get_int("orderId")
            order.clientOrderId = item.get_string("clientOrderId")
            order_list.append(order)
        oco.orders = order_list

        return oco