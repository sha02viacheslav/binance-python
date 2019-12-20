class ExecutionReport:
    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.clientOrderId = ""
        self.side = None
        self.type = None
        self.timeInForce = None
        self.orderQty = 0.0
        self.orderPrice = 0.0
        self.stopPrice = 0.0
        self.icebergQty = 0.0
        self.orderListId = None
        self.origClientOrderId = ""
        self.executionType = ""
        self.orderStatus = ""
        self.errorCode = None
        self.orderId = None
        self.lastExecutedQty = 0.0
        self.cumulativeFilledQty = 0.0
        self.lastExecutedPrice = 0.0
        self.commissionAmount = 0
        self.commissionAsset = None
        self.transactionTime = 0
        self.tradeID = None
        self.ignore = None
        self.isOrderBook = None
        self.isMarkerSide = None
        self.isIgnore = None
        self.orderCreationTime = 0
        self.cumulativeQuoteAssetQty = 0.0
        self.lastQuoteAssetQty = 0.0
        self.quoteOrderQty = 0.0
  
    @staticmethod
    def json_parse(json_data):
        result = ExecutionReport()
        result.eventType = json_data.get_string("e")
        result.eventTime = json_data.get_int("E")
        result.symbol = json_data.get_string("s")
        result.clientOrderId = json_data.get_string("c")
        result.side = json_data.get_string("S")
        result.type = json_data.get_string("o")
        result.timeInForce = json_data.get_string("f")
        result.orderQty = json_data.get_float("q")
        result.orderPrice = json_data.get_float("p")
        result.stopPrice = json_data.get_float("P")
        result.icebergQty = json_data.get_float("F")
        result.orderListId = json_data.get_int("g")
        result.origClientOrderId = json_data.get_string("C")
        result.executionType = json_data.get_string("x")
        result.orderStatus = json_data.get_string("X")
        result.errorCode = json_data.get_string("r")
        result.orderId = json_data.get_int("i")
        result.lastExecutedQty = json_data.get_float("l")
        result.cumulativeFilledQty = json_data.get_float("z")
        result.lastExecutedPrice = json_data.get_float("L")
        result.commissionAmount = json_data.get_int("n")
        result.commissionAsset = json_data.get_string("N")
        result.transactionTime = json_data.get_int("T")
        result.tradeID = json_data.get_int("t")
        result.ignore = json_data.get_int("I")
        result.isOrderBook = json_data.get_boolean("w")
        result.isMarkerSide = json_data.get_boolean("m")
        result.isIgnore = json_data.get_boolean("M")
        result.orderCreationTime = json_data.get_int("O")
        result.cumulativeQuoteAssetQty = json_data.get_float("Z")
        result.lastQuoteAssetQty = json_data.get_float("Y")
        result.quoteOrderQty = json_data.get_float("Q")
        
        return result