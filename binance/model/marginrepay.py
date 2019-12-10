class MarginRepay:

    def __init__(self):
        self.amount = 0.0
        self.asset = ""
        self.interest = 0.0
        self.principal = 0.0
        self.status = ""
        self.timestamp = 0
        self.txId = None

    @staticmethod
    def json_parse(json_data):
        result = MarginRepay()
        result.amount = json_data.get_float("amount")
        result.asset = json_data.get_string("asset")
        result.interest = json_data.get_float("interest")
        result.principal = json_data.get_float("principal")
        result.status = json_data.get_string("status")
        result.timestamp = json_data.get_int("timestamp")
        result.txId = json_data.get_int("txId")
        return result
