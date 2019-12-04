from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_assets = request_client.get_sub_account_assets(email = "123@test.com", symbol = None)

print("======= Query Sub-account Assets(For Master Account) =======")
PrintMix.print_data(sub_account_assets)
print("============================================================")