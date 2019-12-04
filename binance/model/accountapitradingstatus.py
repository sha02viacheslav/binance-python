class TriggerCondition:

    def __init__(self):
        self.GCR = ""
        self.IFER = ""
        self.UFR = ""

class Indicator:

    def __init__(self):
        self.symbol = ""
        self.informations = list()

    @staticmethod
    def json_parse(json_data):
        indicator = Indicator()

        return indicator

class Information: 
    def __init__(self):
        self.i = ""
        self.c = 0
        self.v = 0.0
        self.t = 0.0

class AccountApiTradingStatus:

    def __init__(self):
        self.isLocked = False
        self.plannedRecoverTime = 0
        self.updateTime = 0
        self.triggerCondition = None
        self.indicators = list()

    @staticmethod
    def json_parse(json_data):
        account_api_trading_status = AccountApiTradingStatus()
        account_api_trading_status.isLocked = json_data.get_boolean("isLocked")
        account_api_trading_status.plannedRecoverTime = json_data.get_int("plannedRecoverTime")
        account_api_trading_status.updateTime = json_data.get_int("updateTime")
        account_api_trading_status.triggerCondition = TriggerCondition()
        account_api_trading_status.triggerCondition.GCR = json_data.get_object("triggerCondition").get_string("GCR")
        account_api_trading_status.triggerCondition.IFER = json_data.get_object("triggerCondition").get_string("IFER")
        account_api_trading_status.triggerCondition.UFR = json_data.get_object("triggerCondition").get_string("UFR")

        list_array = json_data.get_array("indicators")
        indicator_list = list()
        
        for item in list_array.get_items():
            indicator = Indicator()
            indicator.symbol = item.json_object

            val_list = list_array.get_array_at(indicator.symbol)
            for element in val_list.get_items():
                info = Information()
                info.i = element.get_string("i")
                info.c = element.get_int("c")
                info.v = element.get_float("v")
                info.t = element.get_float("t")
                indicator.informations.append(info)

            indicator_list.append(indicator)

        account_api_trading_status.indicators = indicator_list
        return account_api_trading_status