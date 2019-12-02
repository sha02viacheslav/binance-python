from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc


class SubAccountTransfer:

    def __init__(self):
        self.fromEmail = ""
        self.toEmail = ""
        self.asset = ""
        self.qty = ""
        self.time = 0

    @staticmethod
    def json_parse(json_data):
        sub_account_transfer = SubAccountTransfer()
        sub_account_transfer.fromEmail = json_data.get_string("from")
        sub_account_transfer.toEmail = json_data.get_string("to")
        sub_account_transfer.asset = json_data.get_boolean("asset")
        sub_account_transfer.qty = json_data.get_string("qty")
        sub_account_transfer.time = convert_cst_in_millisecond_to_utc(json_data.get_int("time"))
        return sub_account_transfer