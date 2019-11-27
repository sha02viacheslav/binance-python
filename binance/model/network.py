

class Network:

    def __init__(self):
        self.addressRegex = ""
        self.coin = ""
        self.depositDesc = ""
        self.depositEnable = False
        self.isDefault = False
        self.memoRegex = ""
        self.name = ""
        self.network = ""
        self.resetAddressStatus = False
        self.specialTips = ""
        self.withdrawDesc = ""
        self.withdrawEnable = False
        self.withdrawFee = 0.0
        self.withdrawIntegerMultiple = 0.0
        self.withdrawMin = 0.0

    @staticmethod
    def json_parse(json_data):
        network = Network()
        network.addressRegex = json_data.get_string("addressRegex")
        network.coin = json_data.get_string("coin")
        network.depositDesc = json_data.get_string("depositDesc")
        network.depositEnable = json_data.get_boolean("depositEnable")
        network.isDefault = json_data.get_boolean("isDefault")
        network.memoRegex = json_data.get_string("memoRegex")
        network.name = json_data.get_string("name")
        network.network = json_data.get_string("network")
        network.resetAddressStatus = json_data.get_boolean("resetAddressStatus")
        network.specialTips = json_data.get_string_or_default("specialTips", "")
        network.withdrawDesc = json_data.get_string("withdrawDesc")
        network.withdrawEnable = json_data.get_boolean("withdrawEnable")
        network.withdrawFee = json_data.get_float_or_default("withdrawFee", 0.0)
        network.withdrawIntegerMultiple = json_data.get_float("withdrawIntegerMultiple")
        network.withdrawMin = json_data.get_float_or_default("withdrawMin", 0.0)
        return network