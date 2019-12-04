class MarginTradeCoeffVo:

    def __init__(self):
        self.forceLiquidationBar = 0.0
        self.marginCallBar = 0.0
        self.normalBar = 0.0

class MarginUserAssetVo:

    def __init__(self):
        self.asset = ""
        self.borrowed = 0.0
        self.free = 0.0
        self.interest = 0.0
        self.locked = 0.0
        self.netAsset = 0.0

class SubAccountMarginDetail:

    def __init__(self):
        self.email = ""
        self.marginLevel = 0.0
        self.totalAssetOfBtc = 0.0
        self.totalLiabilityOfBtc = 0.0
        self.totalNetAssetOfBtc = 0.0
        self.marginTradeCoeffVo = None
        self.marginUserAssetVoList = list()


    @staticmethod
    def json_parse(json_data):
        sub_account_margin_detail = SubAccountMarginDetail()
        sub_account_margin_detail.email = json_data.get_string("email")
        sub_account_margin_detail.marginLevel = json_data.get_float("marginLevel")
        sub_account_margin_detail.totalAssetOfBtc = json_data.get_float("totalAssetOfBtc")
        sub_account_margin_detail.totalLiabilityOfBtc = json_data.get_float("totalLiabilityOfBtc")
        sub_account_margin_detail.totalNetAssetOfBtc = json_data.get_float("totalNetAssetOfBtc")
        sub_account_margin_detail.marginTradeCoeffVo = MarginTradeCoeffVo()
        sub_account_margin_detail.marginTradeCoeffVo.forceLiquidationBar = json_data.get_object("marginTradeCoeffVo").get_float("forceLiquidationBar")
        sub_account_margin_detail.marginTradeCoeffVo.marginCallBar = json_data.get_object("marginTradeCoeffVo").get_float("marginCallBar")
        sub_account_margin_detail.marginTradeCoeffVo.normalBar = json_data.get_object("marginTradeCoeffVo").get_float("normalBar")

        list_array = json_data.get_array("marginUserAssetVoList")
        marginUserAssetVoList = list()
        
        for item in list_array.get_items():
            marginUserAssetVo = MarginUserAssetVo()
            marginUserAssetVo.asset = item.get_string("asset")
            marginUserAssetVo.borrowed = item.get_float("borrowed")
            marginUserAssetVo.free = item.get_float("free")
            marginUserAssetVo.interest = item.get_float("interest")
            marginUserAssetVo.locked = item.get_float("locked")
            marginUserAssetVo.netAsset = item.get_float("netAsset")
            marginUserAssetVoList.append(marginUserAssetVo)

        sub_account_margin_detail.marginUserAssetVoList = marginUserAssetVoList
        return sub_account_margin_detail
