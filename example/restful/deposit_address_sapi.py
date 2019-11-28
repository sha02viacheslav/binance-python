from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

deposit_address = request_client.deposit_address_sapi(coin = "BTC", network = None)

print("======= Deposit Address (supporting network) (USER_DATA) =======")
PrintMix.print_data(deposit_address)
print("================================================================")
