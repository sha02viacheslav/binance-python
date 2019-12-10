class Asset:

    def __init__(self):
        self.asset = ""
        self.borrowed = 0.0
        self.free = 0.0
        self.interest = 0.0
        self.locked = 0.0
        self.netAsset = 0.0


class MarginAccount:

    def __init__(self):
        self.borrowEnabled = False
        self.marginLevel = 0.0
        self.totalAssetOfBtc = 0.0
        self.totalLiabilityOfBtc = 0.0
        self.totalNetAssetOfBtc = 0.0
        self.tradeEnabled = False
        self.transferEnabled = False
        self.userAssets = list()


    @staticmethod
    def json_parse(json_data):
        result = MarginAccount()
        result.borrowEnabled = json_data.get_boolean("borrowEnabled")
        result.marginLevel = json_data.get_float("marginLevel")
        result.totalAssetOfBtc = json_data.get_float("totalAssetOfBtc")
        result.totalLiabilityOfBtc = json_data.get_float("totalLiabilityOfBtc")
        result.totalNetAssetOfBtc = json_data.get_float("totalNetAssetOfBtc")
        result.tradeEnabled = json_data.get_boolean("tradeEnabled")
        result.transferEnabled = json_data.get_boolean("transferEnabled")

        data_list = json_data.get_array("userAssets")
        element_list = list()
        for item in data_list.get_items():
            element = Asset()
            element.asset = item.get_string("asset")
            element.borrowed = item.get_float("borrowed")
            element.free = item.get_float("free")
            element.interest = item.get_float("interest")
            element.locked = item.get_float("locked")
            element.netAsset = item.get_float("netAsset")
            element_list.append(element)

        result.userAssets = element_list
        return result
