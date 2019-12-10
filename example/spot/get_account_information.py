from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
account_information = request_client.get_account_information()
print("makerCommission: ", account_information.makerCommission)
print("takerCommission: ", account_information.takerCommission)
print("buyerCommission: ", account_information.buyerCommission)
print("sellerCommission: ", account_information.sellerCommission)
print("canTrade: ", account_information.canTrade)
print("canWithdraw: ", account_information.canWithdraw)
print("canDeposit: ", account_information.canDeposit)
print("updateTime: ", account_information.updateTime)
print("accountType: ", account_information.accountType)
print("=== Balances ===")
PrintMix.print_data(account_information.balances)
print("==============")