from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


futures_email = request_client.post_sub_account_enable_futures(email = "123@test.com")

print("======= Enable Futures for Sub-account (For Master Account) =======")
print("Futures Account Email: ", futures_email)
print("==================================================================")
