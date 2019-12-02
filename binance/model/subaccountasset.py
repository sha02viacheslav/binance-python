

class SubAccountAsset:

    def __init__(self):
        self.asset = ""
        self.free = 0.0
        self.locked = 0.0

    @staticmethod
    def json_parse(json_data):
        sub_account_asset = SubAccountAsset()
        sub_account_asset.asset = json_data.get_string("asset")
        sub_account_asset.free = json_data.get_string("free")
        sub_account_asset.locked = json_data.get_boolean("locked")
        return sub_account_asset