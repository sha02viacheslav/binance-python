from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

recent_trades_list = request_client.get_recent_trades_list(symbol="XRPRUB", limit=10)

print("======= Recent Trades List =======")
PrintMix.print_data(recent_trades_list)
print("==================================")
