class TradeEvent:

    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.id = None
        self.price = 0.0
        self.qty = 0.0
        self.buyerOrderId = None
        self.sellerOrderId = None
        self.time = 0
        self.isBuyerMaker = False
        self.ignore = False

    @staticmethod
    def json_parse(json_wrapper):
        trade_event = TradeEvent()
        trade_event.eventType = json_wrapper.get_string("e")
        trade_event.eventTime = json_wrapper.get_int("E")
        trade_event.symbol = json_wrapper.get_string("s")
        trade_event.id = json_wrapper.get_int("t")
        trade_event.price = json_wrapper.get_float("p")
        trade_event.qty = json_wrapper.get_float("q")
        trade_event.buyerOrderId = json_wrapper.get_int("b")
        trade_event.sellerOrderId = json_wrapper.get_int("a")
        trade_event.time = json_wrapper.get_int("T")
        trade_event.isBuyerMaker = json_wrapper.get_boolean("m")
        trade_event.ignore = json_wrapper.get_boolean("M")
        return trade_event