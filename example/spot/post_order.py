from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
order = request_client.post_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity=0.01)
print("symbol: ", order.symbol)
print("orderId: ", order.orderId)
print("orderListId: ", order.orderListId)
print("clientOrderId: ", order.clientOrderId)
print("transactTime: ", order.transactTime)
print("price: ", order.price)
print("origQty: ", order.origQty)
print("executedQty: ", order.executedQty)
print("cummulativeQuoteQty: ", order.cummulativeQuoteQty)
print("status: ", order.status)
print("timeInForce: ", order.timeInForce)
print("type: ", order.type)
print("side: ", order.side)
print("=== Fills ===")
PrintMix.print_data(order.fills)
print("===================")
