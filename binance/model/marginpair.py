

class MarginPair:

    def __init__(self):
        self.id = None
        self.symbol = ""
        self.base = ""
        self.quote = ""
        self.isMarginTrade = False
        self.isBuyAllowed = False
        self.isSellAllowed = False

    @staticmethod
    def json_parse(json_data):
        asset = MarginPair()
        asset.id = json_data.get_int("id")
        asset.symbol = json_data.get_string("symbol")
        asset.base = json_data.get_string("base")
        asset.quote = json_data.get_string("quote")
        asset.isMarginTrade = json_data.get_boolean("isMarginTrade")
        asset.isBuyAllowed = json_data.get_boolean("isBuyAllowed")
        asset.isSellAllowed = json_data.get_boolean("isSellAllowed")
        return asset
