

class DepositAddress:

    def __init__(self):
        self.address = ""
        self.addressTag = ""
        self.asset = ""

    @staticmethod
    def json_parse(json_data):
        deposit_address = DepositAddress()
        deposit_address.address = json_data.get_string("address")
        deposit_address.addressTag = json_data.get_string("addressTag")
        deposit_address.asset = json_data.get_string("asset")
        return deposit_address