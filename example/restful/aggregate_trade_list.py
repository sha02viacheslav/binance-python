from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

aggregate_trades_list = request_client.aggregate_trades_list(symbol="XRPRUB", fromId=None, 
												startTime=None, endTime=None, limit=10)

print("======= Compressed/Aggregate Trades List =======")
PrintMix.print_data(aggregate_trades_list)
print("================================================")
