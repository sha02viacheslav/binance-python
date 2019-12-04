from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

current_average_price = request_client.current_average_price(symbol="XRPRUB")

print("======= Current Average Price =======")
PrintMix.print_data(current_average_price)
print("=====================================")
