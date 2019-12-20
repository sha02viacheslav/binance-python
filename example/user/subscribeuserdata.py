import logging
from binance import RequestClient
from binance import SubscriptionClient
from binance.constant.test import *
from binance.model import *
from binance.exception.binanceapiexception import BinanceApiException

from binance.base.printobject import *

# Start user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
listen_key = request_client.start_user_data_stream(accountType=AccountType.SPOT)
# result = request_client.start_user_data_stream(accountType=AccountType.MARGIN)
print("listenKey: ", listen_key)

# Keep user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.keep_user_data_stream(accountType=AccountType.SPOT, listenKey=listen_key)
# result = request_client.keep_user_data_stream(accountType=AccountType.MARGIN, listenKey=listen_key)
print("Result: ", result)

# Close user data stream
# request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
# result = request_client.close_user_data_stream(accountType=AccountType.SPOT, listenKey=listen_key)
# # result = request_client.close_user_data_stream(accountType=AccountType.MARGIN, listenKey=listen_key)
# print("Result: ", result)

logger = logging.getLogger("binance-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        print("Event ID: ", event)
    elif  data_type == SubscribeMessageType.PAYLOAD:
        if(event.eventType == "outboundAccountInfo"):
            print("Event Type: ", event.eventType)
            print("Event time: ", event.eventTime)
            print("Maker commission rate: ", event.makerCommission)
            print("Taker commission rate: ", event.takerCommission)
            print("Buyer commission rate: ", event.buyerCommission)
            print("Seller commission rate: ", event.sellerCommission)
            print("Can trade?: ", event.canTrade)
            print("Can withdraw?: ", event.canWithdraw)
            print("Can deposit?: ", event.canDeposit)
            print("Time of last account update: ", event.updateTime)
            print("=== Balances ===")
            PrintMix.print_data(event.balances)
            print("================")
        elif(event.eventType == "outboundAccountPosition"):
            print("Event Type: ", event.eventType)
            print("Event time: ", event.eventTime)
            print("Time of last account update: ", event.updateTime)
            print("=== Balances ===")
            PrintMix.print_data(event.balances)
            print("================")
        elif(event.eventType == "balanceUpdate"):
            print("Event Type: ", event.eventType)
            print("Event time: ", event.eventTime)
            print("Asset: ", event.asset)
            print("Balance Delta: ", event.delta)
            print("Clear Time: ", event.clearTime)
        elif(event.eventType == "executionReport"):
            PrintBasic.print_obj(event)
        elif(event.eventType == "listStatus"):
            print("Event Type: ", event.eventType)
            print("Event time: ", event.eventTime)
            print("Symbol: ", event.symbol)
            print("OrderListId: ", event.orderListId)
            print("Contingency Type: ", event.contingencyType)
            print("List Status Type: ", event.listStatusType)
            print("List Order Status: ", event.listOrderStatus)
            print("List Reject Reason: ", event.listRejectReason)
            print("List Client Order ID: ", event.listClientOrderId)
            print("Transaction Time: ", event.transactionTime)
            print("=== Orders ===")
            PrintMix.print_data(event.orders)
    else:
        print("Unknown Data:")
    print()


def error(e: 'BinanceApiException'):
    print(e.error_code + e.error_message)

sub_client.subscribe_user_data_event(listen_key, callback, error)