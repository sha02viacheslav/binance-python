from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
asset = request_client.get_margin_asset(asset="BTC")
PrintBasic.print_obj(asset)
