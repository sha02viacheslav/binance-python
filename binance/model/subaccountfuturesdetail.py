from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class Asset:

    def __init__(self):
        self.asset = ""
        self.initialMargin = 0.0
        self.maintMargin = 0.0
        self.marginBalance = 0.0
        self.maxWithdrawAmount = 0.0
        self.openOrderInitialMargin = 0.0
        self.positionInitialMargin = 0.0
        self.unrealizedProfit = 0.0
        self.walletBalance = 0.0


class SubAccountFuturesDetail:

    def __init__(self):
        self.email = ""
        self.canDeposit = False
        self.canTrade = False
        self.canWithdraw = False
        self.feeTier = 0.0
        self.maxWithdrawAmount = 0.0
        self.totalInitialMargin = 0.0
        self.totalMaintMargin = 0.0
        self.totalMarginBalance = 0.0
        self.totalOpenOrderInitialMargin = 0.0
        self.totalPositionInitialMargin = 0.0
        self.totalUnrealizedProfit = 0.0
        self.totalWalletBalance = 0.0
        self.asset = ""
        self.updateTime = 0
        self.assets = list()

 
    @staticmethod
    def json_parse(json_data):
        sub_account_futures_detail = SubAccountFuturesDetail()
        sub_account_futures_detail.email = json_data.get_string("email")
        sub_account_futures_detail.canDeposit = json_data.get_boolean("canDeposit")
        sub_account_futures_detail.canTrade = json_data.get_boolean("canTrade")
        sub_account_futures_detail.canWithdraw = json_data.get_boolean("canWithdraw")
        sub_account_futures_detail.feeTier = json_data.get_float("feeTier")
        sub_account_futures_detail.maxWithdrawAmount = json_data.get_float("maxWithdrawAmount")
        sub_account_futures_detail.totalInitialMargin = json_data.get_float("totalInitialMargin")
        sub_account_futures_detail.totalMaintMargin = json_data.get_float("totalMaintMargin")
        sub_account_futures_detail.totalMarginBalance = json_data.get_float("totalMarginBalance")
        sub_account_futures_detail.totalOpenOrderInitialMargin = json_data.get_float("totalOpenOrderInitialMargin")
        sub_account_futures_detail.totalPositionInitialMargin = json_data.get_float("totalPositionInitialMargin")
        sub_account_futures_detail.totalUnrealizedProfit = json_data.get_float("totalUnrealizedProfit")
        sub_account_futures_detail.totalWalletBalance = json_data.get_float("totalWalletBalance")
        sub_account_futures_detail.asset = json_data.get_string("asset")
        sub_account_futures_detail.updateTime = convert_cst_in_millisecond_to_utc(json_data.get_int("updateTime"))
        
        list_array = json_data.get_array("assets")
        asset_list = list()
        
        for item in list_array.get_items():
            asset = Asset()
            asset.asset = item.get_string("asset")
            asset.initialMargin = item.get_float("initialMargin")
            asset.maintMargin = item.get_float("maintMargin")
            asset.marginBalance = item.get_float("marginBalance")
            asset.maxWithdrawAmount = item.get_float("maxWithdrawAmount")
            asset.openOrderInitialMargin = item.get_float("openOrderInitialMargin")
            asset.positionInitialMargin = item.get_float("positionInitialMargin")
            asset.unrealizedProfit = item.get_float("unrealizedProfit")
            asset.walletBalance = item.get_float("walletBalance")
            asset_list.append(asset)

        sub_account_futures_detail.assets = asset_list
        return sub_account_futures_detail