class BalanceUpdate:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.asset = ""
        self.delta = 0
        self.clearTime = 0
  
    @staticmethod
    def json_parse(json_data):
        result = BalanceUpdate()
        result.eventType = json_data.get_string("e")
        result.eventTime = json_data.get_int("E")
        result.asset = json_data.get_string("a")
        result.delta = json_data.get_float("d")
        result.clearTime = json_data.get_int("T")
        
        return result