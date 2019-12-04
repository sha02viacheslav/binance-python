class SubAccountStatus:

    def __init__(self):
        self.email = ""
        self.isSubUserEnabled = False
        self.isUserActive = False
        self.insertTime = 0
        self.isMarginEnabled = False
        self.isFutureEnabled = False
        self.mobile = 0

    @staticmethod
    def json_parse(json_data):
        sub_account_status = SubAccountStatus()
        sub_account_status.email = json_data.get_string("email")
        sub_account_status.isSubUserEnabled = json_data.get_string("isSubUserEnabled")
        sub_account_status.isUserActive = json_data.get_boolean("isUserActive")
        sub_account_status.insertTime = json_data.get_int("insertTime")
        sub_account_status.isMarginEnabled = json_data.get_string("isMarginEnabled")
        sub_account_status.isFutureEnabled = json_data.get_string("isFutureEnabled")
        sub_account_status.mobile = json_data.get_int("mobile")
        return sub_account_status