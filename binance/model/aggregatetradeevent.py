class AggregateTradeEvent:

    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.id = None
        self.price = 0.0
        self.qty = 0.0
        self.firstId = None
        self.lastId = None
        self.time = 0
        self.isBuyerMaker = False
        self.ignore = False

    @staticmethod
    def json_parse(json_wrapper):
        aggregate_trade_event = AggregateTradeEvent()
        aggregate_trade_event.eventType = json_wrapper.get_string("e")
        aggregate_trade_event.eventTime = json_wrapper.get_int("E")
        aggregate_trade_event.symbol = json_wrapper.get_string("s")
        aggregate_trade_event.id = json_wrapper.get_int("a")
        aggregate_trade_event.price = json_wrapper.get_float("p")
        aggregate_trade_event.qty = json_wrapper.get_float("q")
        aggregate_trade_event.firstId = json_wrapper.get_int("f")
        aggregate_trade_event.lastId = json_wrapper.get_int("l")
        aggregate_trade_event.time = json_wrapper.get_int("T")
        aggregate_trade_event.isBuyerMaker = json_wrapper.get_boolean("m")
        aggregate_trade_event.ignore = json_wrapper.get_boolean("M")
        return aggregate_trade_event