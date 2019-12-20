class Balance:

    def __init__(self):
        self.asset = ""
        self.free = 0.0
        self.locked = 0.0

    @staticmethod
    def json_parse(json_data):
        result = Balance()
        result.asset = json_data.get_string("a")
        result.free = json_data.get_string("f")
        result.locked = json_data.get_boolean("l")
        return result


class OutboundAccountInfo:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.makerCommission = 0
        self.takerCommission = 0
        self.buyerCommission = 0
        self.sellerCommission = 0
        self.canTrade = False
        self.canWithdraw = False
        self.canDeposit = False
        self.updateTime = 0
        self.balances = list()

    @staticmethod
    def json_parse(json_data):
        result = OutboundAccountInfo()
        result.eventType = json_data.get_string("e")
        result.eventTime = json_data.get_int("E")
        result.makerCommission = json_data.get_int("m")
        result.takerCommission = json_data.get_int("t")
        result.buyerCommission = json_data.get_int("b")
        result.sellerCommission = json_data.get_int("s")
        result.canTrade = json_data.get_boolean("T")
        result.canWithdraw = json_data.get_boolean("W")
        result.canDeposit = json_data.get_boolean("D")
        result.updateTime = json_data.get_int("u")
        
        element_list = list()
        data_list = json_data.get_array("B")
        for item in data_list.get_items():
            element = Balance.json_parse(item)
            element_list.append(element)
        result.balances = element_list
        return result