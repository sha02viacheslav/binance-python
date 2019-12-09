import urllib.parse

from binance.constant.system import WebSocketDefine
from binance.impl.websocketrequestimpl import WebsocketRequestImpl
from binance.impl.websocketconnection import WebsocketConnection
from binance.impl.websocketwatchdog import WebSocketWatchDog
from binance.impl.restapirequestimpl import RestApiRequestImpl
from binance.model import *

# For develop
from binance.base.printobject import *

class SubscriptionClient(object):

    def __init__(self, **kwargs):
        """
        Create the subscription client to subscribe the update from server.

        :param kwargs: The option of subscription connection.
            api_key: The public key applied from Binance.
            secret_key: The private key applied from Binance.
            uri: Set the URI for subscription.
            is_auto_connect: When the connection lost is happening on the subscription line, specify whether the client
                            reconnect to server automatically. The connection lost means:
                                Caused by network problem
                                The connection close triggered by server (happened every 24 hours)
                            No any message can be received from server within a specified time, see receive_limit_ms
            receive_limit_ms: Set the receive limit in millisecond. If no message is received within this limit time,
                            the connection will be disconnected.
            connection_delay_failure: If auto reconnect is enabled, specify the delay time before reconnect.
        """
        api_key = None
        secret_key = None
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            secret_key = kwargs["secret_key"]
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.websocket_request_impl = WebsocketRequestImpl(self.__api_key)
        self.connections = list()
        self.uri = WebSocketDefine.Uri
        is_auto_connect = True
        receive_limit_ms = 60000
        connection_delay_failure = 15
        if "uri" in kwargs:
            self.uri = kwargs["uri"]
        if "is_auto_connect" in kwargs:
            is_auto_connect = kwargs["is_auto_connect"]
        if "receive_limit_ms" in kwargs:
            receive_limit_ms = kwargs["receive_limit_ms"]
        if "connection_delay_failure" in kwargs:
            connection_delay_failure = kwargs["connection_delay_failure"]
        self.__watch_dog = WebSocketWatchDog(is_auto_connect, receive_limit_ms, connection_delay_failure)

    def __create_connection(self, request):
        connection = WebsocketConnection(self.__api_key, self.__secret_key, self.uri, self.__watch_dog, request)
        self.connections.append(connection)
        connection.connect()

    def subscribe_candlestick_event(self, symbol: 'str', interval: 'CandlestickInterval', callback,
                                    error_handler=None):
        """
        Kline/Candlestick Streams

        The Kline/Candlestick Stream push updates to the current klines/candlestick every second.

        Stream Name: <symbol>@kline_<interval>
        """
        request = self.websocket_request_impl.subscribe_candlestick_event(symbol, interval, callback, error_handler)
        self.__create_connection(request)

    def subscribe_aggregate_trade_event(self, symbol: 'str', callback, error_handler=None):
        """
        Aggregate Trade Streams

        The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

        Stream Name: <symbol>@aggTrade
        """
        request = self.websocket_request_impl.subscribe_aggregate_trade_event(symbol, callback, error_handler)
        self.__create_connection(request)
        
    def subscribe_trade_event(self, symbol: 'str', callback, error_handler=None):
        """
        Trade Streams

        The Trade Streams push raw trade information; each trade has a unique buyer and seller.

        Stream Name: <symbol>@trade
        """
        request = self.websocket_request_impl.subscribe_trade_event(symbol, callback, error_handler)
        self.__create_connection(request)
        
    def subscribe_symbol_miniticker_event(self, symbol: 'str', callback, error_handler=None):
        """
        Individual Symbol Mini Ticker Stream

        24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

        Stream Name: <symbol>@miniTicker
        """
        request = self.websocket_request_impl.subscribe_symbol_miniticker_event(symbol, callback, error_handler)
        self.__create_connection(request)
        
    def subscribe_all_miniticker_event(self, callback, error_handler=None):
        """
        All Market Mini Tickers Stream

        24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

        Stream Name: !miniTicker@arr
        """
        request = self.websocket_request_impl.subscribe_all_miniticker_event(callback, error_handler)
        self.__create_connection(request)
 
    def subscribe_symbol_ticker_event(self, symbol: 'str', callback, error_handler=None):
        """
        Individual Symbol Ticker Streams

        24hr rollwing window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

        Stream Name: <symbol>@ticker
        """
        request = self.websocket_request_impl.subscribe_symbol_ticker_event(symbol, callback, error_handler)
        self.__create_connection(request)
       
    def subscribe_all_ticker_event(self, callback, error_handler=None):
        """
        All Market Tickers Stream

        24hr rolling window ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

        Stream Name: !ticker@arr
        """
        request = self.websocket_request_impl.subscribe_all_ticker_event(callback, error_handler)
        self.__create_connection(request)
 
    def subscribe_symbol_bookticker_event(self, symbol: 'str', callback, error_handler=None):
        """
        Individual Symbol Book Ticker Streams

        Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.

        Stream Name: <symbol>@bookTicker
        """
        request = self.websocket_request_impl.subscribe_symbol_bookticker_event(symbol, callback, error_handler)
        self.__create_connection(request)
           
    def subscribe_all_bookticker_event(self, callback, error_handler=None):
        """
        All Book Tickers Stream

        Pushes any update to the best bid or ask's price or quantity in real-time for all symbols.

        Stream Name: !bookTicker
        """
        request = self.websocket_request_impl.subscribe_all_bookticker_event(callback, error_handler)
        self.__create_connection(request)

    def unsubscribe_all(self):
        for conn in self.connections:
            conn.close()
        self.connections.clear()

