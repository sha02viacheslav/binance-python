from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
order_list = request_client.get_all_orders(symbol="RENBTC")
PrintMix.print_data(order_list)
