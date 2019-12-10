from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *
from binance.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.post_margin_order(symbol="BTCUSDT", side=OrderSide.SELL, ordertype=OrderType.MARKET, quantity=0.01)
print("symbol: ", result.symbol)
print("orderId: ", result.orderId)
print("clientOrderId: ", result.clientOrderId)
print("transactTime: ", result.transactTime)
print("price: ", result.price)
print("origQty: ", result.origQty)
print("executedQty: ", result.executedQty)
print("cummulativeQuoteQty: ", result.cummulativeQuoteQty)
print("status: ", result.status)
print("timeInForce: ", result.timeInForce)
print("type: ", result.type)
print("side: ", result.side)
print("=== Fills ===")
PrintMix.print_data(result.fills)
print("===================")
