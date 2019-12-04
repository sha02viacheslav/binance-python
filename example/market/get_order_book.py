from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
order_book = request_client.get_order_book(symbol = "XRPRUB", limit = 10)
print("======= Order Book =======")
print("lastUpdateId: ", order_book.lastUpdateId)
print("=== Bids ===")
PrintMix.print_data(order_book.bids)
print("===================")
print("=== Asks ===")
PrintMix.print_data(order_book.asks)
print("===================")
print("====================================")
