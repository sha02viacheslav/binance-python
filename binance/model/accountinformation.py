from binance.model.constant import *


class Balance:

    def __init__(self):
        self.asset = ""
        self.free = 0.0
        self.locked = 0.0

    @staticmethod
    def json_parse(json_data):
        balance = Balance()
        balance.asset = json_data.get_string("asset")
        balance.free = json_data.get_string("free")
        balance.locked = json_data.get_boolean("locked")
        return balance


class AccountInformation:
    def __init__(self):
        self.makerCommission = 0
        self.takerCommission = 0
        self.buyerCommission = 0
        self.sellerCommission = 0
        self.canTrade = False
        self.canWithdraw = False
        self.canDeposit = False
        self.updateTime = 0
        self.accountType = AccountType.INVALID
        self.balances = list()

    @staticmethod
    def json_parse(json_data):
        account_information = AccountInformation()
        account_information.makerCommission = json_data.get_int("makerCommission")
        account_information.takerCommission = json_data.get_int("takerCommission")
        account_information.buyerCommission = json_data.get_int("buyerCommission")
        account_information.sellerCommission = json_data.get_int("sellerCommission")
        account_information.canTrade = json_data.get_boolean("canTrade")
        account_information.canWithdraw = json_data.get_boolean("canWithdraw")
        account_information.canDeposit = json_data.get_boolean("canDeposit")
        account_information.updateTime = json_data.get_int("updateTime")
        account_information.accountType = json_data.get_string("accountType")
        
        balance_list = list()
        data_list = json_data.get_array("balances")
        for item in data_list.get_items():
            balance = Balance.json_parse(item)
            balance_list.append(balance)
        account_information.balances = balance_list
        return account_information