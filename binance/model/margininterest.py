class MarginInterest:

    def __init__(self):
        self.asset = ""
        self.interest = 0.0
        self.interestAccuredTime = 0
        self.interestRate = 0.0
        self.principal = 0.0
        self.type = ""

    @staticmethod
    def json_parse(json_data):
        result = MarginInterest()
        result.asset = json_data.get_string("asset")
        result.interest = json_data.get_float("interest")
        result.interestAccuredTime = json_data.get_int("interestAccuredTime")
        result.interestRate = json_data.get_float("interestRate")
        result.principal = json_data.get_float("principal")
        result.type = json_data.get_string("type")
        return result
