from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

# ticker_price_change_statistics = request_client.ticker_price_change_statistics()
ticker_price_change_statistics = request_client.ticker_price_change_statistics(symbol="XRPRUB")

print("======= 24hr Ticker Price Change Statistics =======")
PrintMix.print_data(ticker_price_change_statistics)
print("===================================================")
