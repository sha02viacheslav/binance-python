from binance.model.network import Network


class CoinInformation:

    def __init__(self):
        self.coin = ""
        self.depositAllEnable = False
        self.free = 0.0
        self.freeze = 0.0
        self.ipoable = 0.0
        self.ipoing = 0.0
        self.isLegalMoney = False
        self.locked = 0.0
        self.name = ""
        self.storage = 0.0
        self.trading = False
        self.withdrawAllEnable = False
        self.withdrawing = 0.0
        self.network_list = list()

    @staticmethod
    def json_parse(json_data):
        coin_information = CoinInformation()
        coin_information.coin = json_data.get_string("coin")
        coin_information.depositAllEnable = json_data.get_boolean("depositAllEnable")
        coin_information.free = json_data.get_float("free")
        coin_information.freeze = json_data.get_float("freeze")
        coin_information.ipoable = json_data.get_float("ipoable")
        coin_information.ipoing = json_data.get_float("ipoing")
        coin_information.isLegalMoney = json_data.get_boolean("isLegalMoney")
        coin_information.locked = json_data.get_float("locked")
        coin_information.name = json_data.get_string("name")
        coin_information.storage = json_data.get_float("storage")
        coin_information.trading = json_data.get_boolean("trading")
        coin_information.withdrawAllEnable = json_data.get_boolean("withdrawAllEnable")
        coin_information.withdrawing = json_data.get_float("withdrawing")
        list_array = json_data.get_array("networkList")
        network_list = list()
        for item in list_array.get_items():
            network = Network.json_parse(item)
            network_list.append(network)

        coin_information.network_list = network_list

        return coin_information

