from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class DepositHistory:

    def __init__(self):
        self.insertTime = 0
        self.amount = 0.0
        self.asset = ""
        self.address = ""
        self.txId = ""
        self.status = None

    @staticmethod
    def json_parse(json_data):
        deposit_history = DepositHistory()
        deposit_history.insertTime = convert_cst_in_millisecond_to_utc(json_data.get_int("insertTime"))
        deposit_history.amount = json_data.get_float("amount")
        deposit_history.asset = json_data.get_string("asset")
        deposit_history.address = json_data.get_string("address")
        deposit_history.txId = json_data.get_string("txId")
        deposit_history.status = json_data.get_int("status")
        return deposit_history