from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
oco = request_client.post_oco(symbol="RENBTC", side=OrderSide.BUY, quantity=99, price=0.00000481, stopPrice=0.00000480)
print("orderListId: ", oco.orderListId)
print("contingencyType: ", oco.contingencyType)
print("listStatusType: ", oco.listStatusType)
print("listClientOrderId: ", oco.listClientOrderId)
print("transactionTime: ", oco.transactionTime)
print("symbol: ", oco.symbol)
print("=== Orders ===")
PrintMix.print_data(oco.orders)
print("==============")
print("=== Order Reports ===")
PrintMix.print_data(oco.orderReports)
print("=====================")