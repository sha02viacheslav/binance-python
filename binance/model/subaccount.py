class SubAccount:

    def __init__(self):
        self.email = ""
        self.status = ""
        self.activated = False
        self.mobile = ""
        self.gAuth = False
        self.createTime = 0

    @staticmethod
    def json_parse(json_data):
        sub_account = SubAccount()
        sub_account.email = json_data.get_string("email")
        sub_account.status = json_data.get_string("status")
        sub_account.activated = json_data.get_boolean("activated")
        sub_account.mobile = json_data.get_string("mobile")
        sub_account.gAuth = json_data.get_boolean("gAuth")
        sub_account.createTime = json_data.get_int("createTime")
        return sub_account