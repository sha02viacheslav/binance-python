from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class SubAccount:

    def __init__(self):
        self.email = ""
        self.totalAssetOfBtc = 0.0
        self.totalLiabilityOfBtc = 0.0
        self.totalNetAssetOfBtc = 0.0

class SubAccountMarginSummary:

    def __init__(self):
        self.totalAssetOfBtc = 0.0
        self.totalLiabilityOfBtc = 0.0
        self.totalNetAssetOfBtc = 0.0
        self.subAccountList = list()


    @staticmethod
    def json_parse(json_data):
        sub_account_margin_summary = SubAccountMarginSummary()
        sub_account_margin_summary.totalAssetOfBtc = json_data.get_float("totalAssetOfBtc")
        sub_account_margin_summary.totalLiabilityOfBtc = json_data.get_float("totalLiabilityOfBtc")
        sub_account_margin_summary.totalNetAssetOfBtc = json_data.get_float("totalNetAssetOfBtc")

        list_array = json_data.get_array("subAccountList")
        sub_account_list = list()
        
        for item in list_array.get_items():
            sub_account = SubAccount()
            sub_account.email = item.get_string("email")
            sub_account.totalAssetOfBtc = item.get_float("totalAssetOfBtc")
            sub_account.totalLiabilityOfBtc = item.get_float("totalLiabilityOfBtc")
            sub_account.totalNetAssetOfBtc = item.get_float("totalNetAssetOfBtc")
            sub_account_list.append(sub_account)

        sub_account_margin_summary.subAccountList = sub_account_list
        return sub_account_margin_summary
