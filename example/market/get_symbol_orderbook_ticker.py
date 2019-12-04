from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# symbol_orderbook_ticker = request_client.symbol_orderbook_ticker()
symbol_orderbook_ticker = request_client.get_symbol_orderbook_ticker(symbol="XRPRUB")

print("======= Symbol Order Book Ticker =======")
PrintMix.print_data(symbol_orderbook_ticker)
print("===================================")
