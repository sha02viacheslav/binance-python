from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
exchange_information = request_client.exchange_information()
print("======= Exchange Information =======")
print("timezone: ", exchange_information.timezone)
print("serverTime: ", exchange_information.serverTime)
print("=== Rate Limits ===")
PrintMix.print_data(exchange_information.rateLimits)
print("===================")
print("=== Exchange Filters ===")
PrintMix.print_data(exchange_information.exchangeFilters)
print("===================")
print("=== Symbols ===")
PrintMix.print_data(exchange_information.symbols)
print("===================")
print("====================================")
