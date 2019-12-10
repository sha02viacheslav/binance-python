class Order:

    def __init__(self):
        self.symbol = ""
        self.orderId = None
        self.clientOrderId = ""


class Report:

    def __init__(self):
        self.symbol = ""
        self.origClientOrderId = None
        self.orderId = None
        self.orderListId = None
        self.clientOrderId = None
        self.price = None
        self.origQty = None
        self.executedQty = None
        self.cummulativeQuoteQty = None
        self.status = None
        self.timeInForce = None
        self.type = None
        self.side = None
        self.stopPrice = None


class CancelOco:

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
        oco = CancelOco()
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
    
        list_array = json_data.get_array("orderReports")
        report_list = list()
        for item in list_array.get_items():
            report = Report()
            report.symbol = item.get_string("symbol")
            report.origClientOrderId = item.get_string("origClientOrderId")
            report.orderId = item.get_int("orderId")
            report.orderListId = item.get_int("orderListId")
            report.clientOrderId = item.get_string("clientOrderId")
            report.price = item.get_float("price")
            report.origQty = item.get_float("origQty")
            report.executedQty = item.get_float("executedQty")
            report.cummulativeQuoteQty = item.get_float("cummulativeQuoteQty")
            report.status = item.get_string("status")
            report.timeInForce = item.get_string("timeInForce")
            report.type = item.get_string("type")
            report.side = item.get_string("side")
            report.stopPrice = item.get_float_or_default("stopPrice", 0.0)
            report_list.append(order)
        oco.orderReports = report_list 

        return oco
