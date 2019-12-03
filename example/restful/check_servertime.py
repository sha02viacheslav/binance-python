from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
server_time = request_client.check_servertime()
print("======= Check Server Time =======")
PrintMix.print_data(server_time)
print("=================================")
