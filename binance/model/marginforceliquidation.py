class MarginForceLiquidation:

    def __init__(self):
        self.avgPrice = 0.0
        self.executedQty = 0.0
        self.orderId = None
        self.price = 0.0
        self.qty = 0.0
        self.side = None
        self.symbol = ""
        self.timeInForce = ""
        self.updatedTime = 0

    @staticmethod
    def json_parse(json_data):
        result = MarginForceLiquidation()
        result.avgPrice = json_data.get_float("avgPrice")
        result.executedQty = json_data.get_float("executedQty")
        result.orderId = json_data.get_int("orderId")
        result.price = json_data.get_float("price")
        result.qty = json_data.get_float("qty")
        result.side = json_data.get_string("side")
        result.symbol = json_data.get_string("symbol")
        result.timeInForce = json_data.get_string("timeInForce")
        result.updatedTime = json_data.get_int("updatedTime")
        return result
