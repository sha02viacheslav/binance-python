from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


txnId = request_client.post_sub_account_transfer(fromEmail = "123@test.com", toEmail = "123@test.com", 
                                            asset = "BTC", amount = 0.1)

print("======= Sub-account Transfer(For Master Account) =======")
print("Transaction ID: ", txnId)
print("========================================================")



