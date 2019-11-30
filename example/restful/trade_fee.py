from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

trade_fee_list = request_client.trade_fee(symbol = "ZRXUSDT")

print("======= Trade Fee (USER_DATA) =======")
PrintMix.print_data(trade_fee_list)
print("=====================================")