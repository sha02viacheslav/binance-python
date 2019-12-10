from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_margin_account()
print("borrowEnabled: ", result.borrowEnabled)
print("marginLevel: ", result.marginLevel)
print("totalAssetOfBtc: ", result.totalAssetOfBtc)
print("totalLiabilityOfBtc: ", result.totalLiabilityOfBtc)
print("totalNetAssetOfBtc: ", result.totalNetAssetOfBtc)
print("tradeEnabled: ", result.tradeEnabled)
print("transferEnabled: ", result.transferEnabled)
print("userAssets:")
PrintMix.print_data(result.userAssets)

