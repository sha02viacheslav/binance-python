from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

account_status = request_client.get_account_status()

print("======= Account Status (USER_DATA) =======")
PrintMix.print_data(account_status)
print("==========================================")





