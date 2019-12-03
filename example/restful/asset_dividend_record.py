from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

asset_dividend_record = request_client.asset_dividend_record(asset = None, startTime = None, endTime = None)

print("======= Asset Dividend Record (USER_DATA) =======")
print("Total: ", asset_dividend_record.total)
print("=== Record ===")
PrintMix.print_data(asset_dividend_record.rows)
print("=======================")
print("=================================================")