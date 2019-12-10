class MarginLoan:

    def __init__(self):
        self.asset = ""
        self.principal = 0.0
        self.timestamp = 0
        self.status = ""

    @staticmethod
    def json_parse(json_data):
        result = MarginLoan()
        result.asset = json_data.get_string("asset")
        result.principal = json_data.get_float("principal")
        result.timestamp = json_data.get_int("timestamp")
        result.status = json_data.get_string("status")
        return result
