class TickerPriceChangeStatistics:

    def __init__(self):
        self.symbol = ""
        self.priceChange = 0.0
        self.priceChangePercent = 0.0
        self.weightedAvgPrice = 0.0
        self.prevClosePrice = 0.0
        self.lastPrice = 0.0
        self.lastQty = 0.0
        self.bidPrice = 0.0
        self.askPrice = 0.0
        self.openPrice = 0.0
        self.highPrice = 0.0
        self.lowPrice = 0.0
        self.volume = 0.0
        self.quoteVolume = 0.0
        self.openTime = 0
        self.closeTime = 0
        self.firstId = None
        self.lastId = None
        self.count = None

    @staticmethod
    def json_parse(json_data):
        ticker_price_change = TickerPriceChangeStatistics()
        ticker_price_change.symbol = json_data.get_string("symbol")
        ticker_price_change.priceChange = json_data.get_float("priceChange")
        ticker_price_change.priceChangePercent = json_data.get_float("priceChangePercent")
        ticker_price_change.weightedAvgPrice = json_data.get_float("weightedAvgPrice")
        ticker_price_change.prevClosePrice = json_data.get_float("prevClosePrice")
        ticker_price_change.lastPrice = json_data.get_float("lastPrice")
        ticker_price_change.lastQty = json_data.get_float("lastQty")
        ticker_price_change.bidPrice = json_data.get_float("bidPrice")
        ticker_price_change.askPrice = json_data.get_float("askPrice")
        ticker_price_change.openPrice = json_data.get_float("openPrice")
        ticker_price_change.highPrice = json_data.get_float("highPrice")
        ticker_price_change.lowPrice = json_data.get_float("lowPrice")
        ticker_price_change.volume = json_data.get_float("volume")
        ticker_price_change.quoteVolume = json_data.get_float("quoteVolume")
        ticker_price_change.openTime = json_data.get_int("openTime")
        ticker_price_change.closeTime = json_data.get_int("closeTime")
        ticker_price_change.firstId = json_data.get_int("firstId")
        ticker_price_change.lastId = json_data.get_int("lastId")
        ticker_price_change.count = json_data.get_int("count")
        return ticker_price_change