from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
system_status = request_client.system_status()
print("======= System Status (System) =======")
PrintMix.print_data(system_status)
print("======================================")


