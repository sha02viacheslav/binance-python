from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

account_api_trading_status = request_client.account_api_trading_status()

print("======= Account API Trading Status (USER_DATA) =======")
print("isLocked: ", account_api_trading_status.isLocked)
print("plannedRecoverTime: ", account_api_trading_status.plannedRecoverTime)
print("updateTime: ", account_api_trading_status.updateTime)
print("=== Triger Condition ===")
print("\tNumber of GTC orders: ", account_api_trading_status.triggerCondition.GCR)
print("\tNumber of FOK/IOC orders: ", account_api_trading_status.triggerCondition.IFER)
print("\tNumber of orders: ", account_api_trading_status.triggerCondition.UFR)
print("========================")
print("")
for indicator in account_api_trading_status.indicators:
	print("Symbol: ", indicator.symbol)
	for information in indicator.informations:
		print("")
		print("\tCount of ", information.i, " orders: ", information.c)
		print("\tCurrent ", information.i, " value: ", information.v)
		print("\tTrigger ", information.i, " value: ", information.t)
	print("")
print("======================================================")





