class DepositHistorySapi:

    def __init__(self):
        self.address = ""
        self.addressTag = ""
        self.amount = 0.0
        self.coin = ""
        self.insertTime = 0
        self.network = ""
        self.status = None
        self.txId = ""

    @staticmethod
    def json_parse(json_data):
        deposit_history = DepositHistorySapi()
        deposit_history.address = json_data.get_string("address")
        deposit_history.addressTag = json_data.get_string("addressTag")
        deposit_history.amount = json_data.get_float("amount")
        deposit_history.coin = json_data.get_string("coin")
        deposit_history.insertTime = json_data.get_int("insertTime")
        deposit_history.network = json_data.get_string("network")
        deposit_history.status = json_data.get_int("status")
        deposit_history.txId = json_data.get_string("txId")
        return deposit_history