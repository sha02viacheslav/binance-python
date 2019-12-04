from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

asset_detail_list = request_client.get_asset_detail()

print("======= Trade Fee (USER_DATA) =======")
PrintMix.print_data(asset_detail_list)
print("=====================================")