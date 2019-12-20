from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
order = request_client.cancel_order(symbol="RENBTC", orderId=37473358)
PrintBasic.print_obj(order)
