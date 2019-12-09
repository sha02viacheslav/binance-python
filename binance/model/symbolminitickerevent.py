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
        symbol_miniticker_event = SymbolMiniTickerEvent()
        symbol_miniticker_event.eventType = json_wrapper.get_string("e")
        symbol_miniticker_event.eventTime = json_wrapper.get_int("E")
        symbol_miniticker_event.symbol = json_wrapper.get_string("s")
        symbol_miniticker_event.open = json_wrapper.get_float("o")
        symbol_miniticker_event.close = json_wrapper.get_float("c")
        symbol_miniticker_event.high = json_wrapper.get_float("h")
        symbol_miniticker_event.low = json_wrapper.get_float("l")
        symbol_miniticker_event.totalTradedBaseAssetVolume = json_wrapper.get_float("v")
        symbol_miniticker_event.totalTradedQuoteAssetVolume = json_wrapper.get_float("q")
        return symbol_miniticker_event