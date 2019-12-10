

class MarginAsset:

    def __init__(self):
        self.assetFullName = ""
        self.assetName = ""
        self.isBorrowable = False
        self.isMortgageable = False
        self.userMinBorrow = 0.0
        self.userMinRepay = 0.0

    @staticmethod
    def json_parse(json_data):
        asset = MarginAsset()
        asset.assetFullName = json_data.get_string("assetFullName")
        asset.assetName = json_data.get_string("assetName")
        asset.isBorrowable = json_data.get_boolean("isBorrowable")
        asset.isMortgageable = json_data.get_boolean("isMortgageable")
        asset.userMinBorrow = json_data.get_float("userMinBorrow")
        asset.userMinRepay = json_data.get_float("userMinRepay")
        return asset
