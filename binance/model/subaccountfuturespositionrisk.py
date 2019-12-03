

class SubAccountFuturesPositionrisk:

    def __init__(self):
        self.entryPrice = 0.0
        self.leverage = 0.0
        self.maxNotional = 0.0
        self.liquidationPrice = 0.0
        self.markPrice = 0.0
        self.positionAmt = 0.0
        self.symbol = ""
        self.unRealizedProfit = 0.0

    @staticmethod
    def json_parse(json_data):
        sub_account_futures_positionrisk = SubAccountFuturesPositionrisk()
        sub_account_futures_positionrisk.entryPrice = json_data.get_float("entryPrice")
        sub_account_futures_positionrisk.leverage = json_data.get_float("leverage")
        sub_account_futures_positionrisk.maxNotional = json_data.get_float("maxNotional")
        sub_account_futures_positionrisk.liquidationPrice = json_data.get_float("liquidationPrice")
        sub_account_futures_positionrisk.markPrice = json_data.get_float("markPrice")
        sub_account_futures_positionrisk.positionAmt = json_data.get_float("positionAmt")
        sub_account_futures_positionrisk.symbol = json_data.get_string("symbol")
        sub_account_futures_positionrisk.unRealizedProfit = json_data.get_float("unRealizedProfit")

        return sub_account_futures_positionrisk