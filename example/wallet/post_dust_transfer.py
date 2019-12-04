from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

assets = list()
assets.append("BTC")
assets.append("USDT")

dust_transfer_result = request_client.post_dust_transfer(asset = assets)

print("======= Dust Transfer (USER_DATA) =======")
print("totalServiceCharge: ", dust_transfer_result.totalServiceCharge)
print("totalTransfered: ", dust_transfer_result.totalTransfered)
print("=== Transfer Result ===")
PrintMix.print_data(dust_transfer_result.transferResult)
print("=======================")
print("=========================================")