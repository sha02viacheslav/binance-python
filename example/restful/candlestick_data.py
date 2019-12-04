from binance import RequestClient
from binance.model import *
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

candlestick_data = request_client.candlestick_data(symbol="XRPRUB", interval=CandlestickInterval.MIN1, 
												startTime=None, endTime=None, limit=10)

print("======= Kline/Candlestick Data =======")
PrintMix.print_data(candlestick_data)
print("======================================")
