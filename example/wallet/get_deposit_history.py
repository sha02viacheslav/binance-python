from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

deposit_histories = request_client.get_deposit_history(asset = "BTC", status = None, startTime = None, endTime = None)

print("======= Deposit History (USER_DATA) =======")
PrintMix.print_data(deposit_histories)
print("=================================================================")





