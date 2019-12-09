class SymbolMiniTickerEvent:

    def __init__(self):
        self.eventType = ""
        self.eventTime = 0
        self.symbol = ""
        self.open = 0.0
        self.close = 0.0
        self.high = 0.0
        self.low = 0.0
        self.totalTradedBaseAssetVolume = 0.0
        self.totalTradedQuoteAssetVolume = 0.0

    @staticmethod
    def json_parse(json_wrapper):
        trade_event = SymbolMiniTickerEvent()
        trade_event.eventType = json_wrapper.get_string("e")
        trade_event.eventTime = json_wrapper.get_int("E")
        trade_event.symbol = json_wrapper.get_string("s")
        trade_event.open = json_wrapper.get_float("o")
        trade_event.close = json_wrapper.get_float("c")
        trade_event.high = json_wrapper.get_float("h")
        trade_event.low = json_wrapper.get_float("l")
        trade_event.totalTradedBaseAssetVolume = json_wrapper.get_float("v")
        trade_event.totalTradedQuoteAssetVolume = json_wrapper.get_float("q")
        return trade_event