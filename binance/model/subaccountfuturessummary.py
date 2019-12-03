from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class SubAccount:

    def __init__(self):
        self.email = ""
        self.totalInitialMargin = 0.0
        self.totalMaintMargin = 0.0
        self.totalMarginBalance = 0.0
        self.totalOpenOrderInitialMargin = 0.0
        self.totalPositionInitialMargin = 0.0
        self.totalUnrealizedProfit = 0.0
        self.totalWalletBalance = 0.0
        self.asset = ""


class SubAccountFuturesSummary:

    def __init__(self):
        self.totalInitialMargin = 0.0
        self.totalMaintMargin = 0.0
        self.totalMarginBalance = 0.0
        self.totalOpenOrderInitialMargin = 0.0
        self.totalPositionInitialMargin = 0.0
        self.totalUnrealizedProfit = 0.0
        self.totalWalletBalance = 0.0
        self.asset = ""
        self.subAccount = list()

    @staticmethod
    def json_parse(json_data):
        sub_account_futures_summary = SubAccountFuturesSummary()
        sub_account_futures_summary.totalInitialMargin = json_data.get_float("totalInitialMargin")
        sub_account_futures_summary.totalMaintMargin = json_data.get_float("totalMaintMargin")
        sub_account_futures_summary.totalMarginBalance = json_data.get_float("totalMarginBalance")
        sub_account_futures_summary.totalOpenOrderInitialMargin = json_data.get_float("totalOpenOrderInitialMargin")
        sub_account_futures_summary.totalPositionInitialMargin = json_data.get_float("totalPositionInitialMargin")
        sub_account_futures_summary.totalUnrealizedProfit = json_data.get_float("totalUnrealizedProfit")
        sub_account_futures_summary.totalWalletBalance = json_data.get_float("totalWalletBalance")
        sub_account_futures_summary.asset = json_data.get_string("asset")
        
        list_array = json_data.get_array("subAccount")
        sub_account_list = list()
        
        for item in list_array.get_items():
            sub_account = SubAccount()
            sub_account.email = item.get_string("email")
            sub_account.totalInitialMargin = item.get_float("totalInitialMargin")
            sub_account.totalMaintMargin = item.get_float("totalMaintMargin")
            sub_account.totalMarginBalance = item.get_float("totalMarginBalance")
            sub_account.totalOpenOrderInitialMargin = item.get_float("totalOpenOrderInitialMargin")
            sub_account.totalPositionInitialMargin = item.get_float("totalPositionInitialMargin")
            sub_account.totalUnrealizedProfit = item.get_float("totalUnrealizedProfit")
            sub_account.totalWalletBalance = item.get_float("totalWalletBalance")
            sub_account.asset = item.get_string("asset")
            sub_account_list.append(sub_account)

        sub_account_futures_summary.subAccount = sub_account_list
        return sub_account_futures_summary