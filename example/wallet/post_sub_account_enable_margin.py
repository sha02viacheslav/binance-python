from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


margin_email = request_client.post_sub_account_enable_margin(email = "123@test.com")

print("======= Enable Margin for Sub-account (For Master Account) =======")
print("Margin Account Email: ", margin_email)
print("==================================================================")
