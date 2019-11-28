from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class WithdrawHistory:

    def __init__(self):
        self.id = ""
        self.amount = 0.0
        self.transactionFee = 0.0
        self.address = ""
        self.asset = ""
        self.txId = ""
        self.applyTime = 0
        self.status = None

    @staticmethod
    def json_parse(json_data):
        withdraw_history = WithdrawHistory()
        withdraw_history.id = json_data.get_string("id")
        withdraw_history.amount = json_data.get_float("amount")
        withdraw_history.transactionFee = json_data.get_float("transactionFee")
        withdraw_history.address = json_data.get_string("address")
        withdraw_history.asset = json_data.get_string("asset")
        withdraw_history.txId = json_data.get_string("txId")
        withdraw_history.applyTime = convert_cst_in_millisecond_to_utc(json_data.get_int("applyTime"))
        withdraw_history.status = json_data.get_int("status")
        return withdraw_history