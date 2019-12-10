class MarginTransfer:

    def __init__(self):
        self.amount = 0.0
        self.asset = ""
        self.status = ""
        self.timestamp = 0
        self.txId = None
        self.type = None

    @staticmethod
    def json_parse(json_data):
        result = MarginTransfer()
        result.amount = json_data.get_float("amount")
        result.asset = json_data.get_string("asset")
        result.status = json_data.get_string("status")
        result.timestamp = json_data.get_int("timestamp")
        result.txId = json_data.get_int("txId")
        result.type = json_data.get_string("type")
        return result
