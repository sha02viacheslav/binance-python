from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# symbol_price_ticker = request_client.symbol_price_ticker()
symbol_price_ticker = request_client.symbol_price_ticker(symbol="XRPRUB")

print("======= Symbol Price Ticker =======")
PrintMix.print_data(symbol_price_ticker)
print("===================================")
