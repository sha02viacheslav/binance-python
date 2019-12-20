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


class OutboundAccountPosition:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.updateTime = 0
        self.balances = list()

    @staticmethod
    def json_parse(json_data):
        result = OutboundAccountPosition()
        result.eventType = json_data.get_string("e")
        result.eventTime = json_data.get_int("E")
        result.updateTime = json_data.get_int("u")
        
        element_list = list()
        data_list = json_data.get_array("B")
        for item in data_list.get_items():
            element = Balance.json_parse(item)
            element_list.append(element)
        result.balances = element_list
        return result