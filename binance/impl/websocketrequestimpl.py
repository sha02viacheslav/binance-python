import time
from binance.impl.websocketrequest import WebsocketRequest
from binance.impl.utils.channels import *
from binance.impl.utils.channelparser import ChannelParser
from binance.impl.utils.timeservice import *
from binance.impl.utils.inputchecker import *
from binance.model import *
# from binance.model.candlestickrequest import CandlestickRequest
# For develop
from binance.base.printobject import *


class WebsocketRequestImpl(object):

    def __init__(self, api_key):
        self.__api_key = api_key

    def subscribe_candlestick_event(self, symbol, interval, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(interval, "interval")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(kline_channel(symbol, interval))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            candle_stick_event_obj = CandlestickEvent.json_parse(json_wrapper)
            return candle_stick_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request

    def subscribe_aggregate_trade_event(self, symbol, callback, error_handler=None):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(callback, "callback")

        def subscription_handler(connection):
            connection.send(aggregate_trade_channel(symbol))
            time.sleep(0.01)

        def json_parse(json_wrapper):
            aggregate_trade_event_obj = AggregateTradeEvent.json_parse(json_wrapper)
            return aggregate_trade_event_obj

        request = WebsocketRequest()
        request.subscription_handler = subscription_handler
        request.json_parser = json_parse
        request.update_callback = callback
        request.error_handler = error_handler

        return request