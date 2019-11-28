

class DepositAddressSapi:

    def __init__(self):
        self.address = ""
        self.coin = ""
        self.tag = ""
        self.url = ""

    @staticmethod
    def json_parse(json_data):
        deposit_address = DepositAddressSapi()
        deposit_address.address = json_data.get_string("address")
        deposit_address.coin = json_data.get_string("coin")
        deposit_address.tag = json_data.get_string("tag")
        deposit_address.url = json_data.get_string("url")
        return deposit_address