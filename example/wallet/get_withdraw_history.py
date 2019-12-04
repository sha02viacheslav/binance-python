from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

withdraw_histories = request_client.get_withdraw_history(asset = "BTC", status = None, startTime = None, endTime = None)

print("======= Withdraw History (USER_DATA) =======")
PrintMix.print_data(withdraw_histories)
print("=================================================================")





