from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

old_trade_lookup = request_client.old_trade_lookup(symbol="XRPRUB", limit=10, fromId=None)

print("======= Old Trade Lookup =======")
PrintMix.print_data(old_trade_lookup)
print("==================================")
