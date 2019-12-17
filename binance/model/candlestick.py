class Candlestick:

    def __init__(self):
        self.openTime = 0
        self.open = 0.0
        self.high = 0.0
        self.low = 0.0
        self.close = 0.0
        self.volume = 0.0
        self.closeTime = 0
        self.quoteAssetVolume = 0.0
        self.numTrades = 0
        self.takerBuyBaseAssetVolume = 0.0
        self.takerBuyQuoteAssetVolume = 0.0
        self.ignore = 0.0

    @staticmethod
    def json_parse(json_data):
        data_obj = Candlestick()
        val = json_data.convert_2_list()
        data_obj.openTime = val[0]
        data_obj.open = val[1]
        data_obj.high = val[2]
        data_obj.low = val[3]
        data_obj.close = val[4]
        data_obj.volume = val[5]
        data_obj.closeTime = val[6]
        data_obj.quoteAssetVolume = val[7]
        data_obj.numTrades = val[8]
        data_obj.takerBuyBaseAssetVolume = val[9]
        data_obj.takerBuyQuoteAssetVolume = val[10]
        data_obj.ignore = val[11]
  
        return data_obj