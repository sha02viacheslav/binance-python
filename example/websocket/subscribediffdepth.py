import logging
from binance import SubscriptionClient
from binance.constant.test import *
from binance.model import *
from binance.exception.binanceapiexception import BinanceApiException

from binance.base.printobject import *

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
        print("Event Type: ", event.eventType)
        print("Event Time: ", event.eventTime)
        print("Symbol: ", event.symbol)
        print("First update ID in event: ", event.firstUpdateId)
        print("Final update ID in event: ", event.finalUpdateId)
        print("=== Bids to be updated ===")
        PrintMix.print_data(event.bids)
        print("==========================")
        print("=== Asks to be updated ===")
        PrintMix.print_data(event.asks)
        print("==========================")
        sub_client.unsubscribe_all()
    else:
        print("Unknown Data:")
    print()


def error(e: 'BinanceApiException'):
    print(e.error_code + e.error_message)

sub_client.subscribe_diff_depth_event("btcusdt", callback, error)