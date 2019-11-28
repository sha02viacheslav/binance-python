from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class WithdrawHistorySapi:

    def __init__(self):
        self.address = ""
        self.amount = 0.0
        self.applyTime = ""
        self.coin = ""
        self.id = ""
        self.network = ""
        self.status = None
        self.txId = ""

    @staticmethod
    def json_parse(json_data):
        withdraw_history = WithdrawHistorySapi()
        withdraw_history.address = json_data.get_string("address")
        withdraw_history.amount = json_data.get_float("amount")
        withdraw_history.applyTime = json_data.get_srting("applyTime")
        withdraw_history.coin = json_data.get_string("coin")
        withdraw_history.id = json_data.get_string("id")
        withdraw_history.network = json_data.get_string("network")
        withdraw_history.status = json_data.get_int("status")
        withdraw_history.txId = json_data.get_string("txId")
        return withdraw_history