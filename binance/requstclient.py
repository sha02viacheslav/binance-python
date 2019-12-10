from binance.constant.system import RestApiDefine
from binance.impl.restapirequestimpl import RestApiRequestImpl
from binance.impl.restapiinvoker import call_sync
from binance.model.constant import *


class RequestClient(object):

    def __init__(self, **kwargs):
        """
        Create the request client instance.
        :param kwargs: The option of request connection.
            api_key: The public key applied from Binance.
            secret_key: The private key applied from Binance.
            server_url: The URL name like "https://api.binance.com".
        """
        api_key = None
        secret_key = None
        url = RestApiDefine.Url
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
        if "secret_key" in kwargs:
            secret_key = kwargs["secret_key"]
        if "url" in kwargs:
            url = kwargs["url"]
        try:
            self.request_impl = RestApiRequestImpl(api_key, secret_key, url)
        except Exception:
            pass

    def get_system_status(self) -> any:
        """
        System status (System)
        
        GET /wapi/v3/systemStatus.html

        Get the system status.
        """
        return call_sync(self.request_impl.get_system_status())

    def get_all_coins_information(self) -> any:
        """
        All Coins' Information (USER_DATA)

        GET /sapi/v1/capital/config/getall (HMAC SHA256)

        Get all coins' information for user.
        """
        return call_sync(self.request_impl.get_all_coins_information())

    def post_withdraw_sapi(self, coin: 'str', address: 'str', amount: 'float', network: 'str' = None, 
                        addressTag: 'str' = None, name: 'str' = None) -> str:
        """
        Withdraw [SAPI]

        POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)

        Submit a withdraw request.
        """
        return call_sync(self.request_impl.post_withdraw_sapi(coin, address, amount, network, addressTag, name))

    def post_withdraw(self, asset: 'str', address: 'str', amount: 'float', network: 'str' = None, 
                        addressTag: 'str' = None, name: 'str' = None) -> str:
        """
        Withdraw

        POST /wapi/v3/withdraw.html (HMAC SHA256)

        Submit a withdraw request.
        """
        return call_sync(self.request_impl.post_withdraw(asset, address, amount, network, addressTag, name))

    def get_deposit_history_sapi(self, coin: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None, offest: 'int' = None) -> any:
        """
        Deposit History（supporting network） (USER_DATA)

        GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)

        Fetch deposit history.
        """
        return call_sync(self.request_impl.get_deposit_history_sapi(coin, status, startTime, endTime, offest))

    def get_deposit_history(self, asset: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None) -> any:
        """
        Deposit History (USER_DATA)

        GET /wapi/v3/depositHistory.html (HMAC SHA256)

        Fetch deposit history.
        """
        return call_sync(self.request_impl.get_deposit_history(asset, status, startTime, endTime))
    
    def get_withdraw_history_sapi(self, coin: 'str' = None, status: 'int' = None, offset: 'int' = None, limit: 'int' = None, 
                                startTime: 'long' = None, endTime: 'long' = None) -> any:
        """
        Withdraw History (supporting network) (USER_DATA)

        Get /sapi/v1/capital/withdraw/history (HMAC SHA256)

        Fetch withdraw history.
        """
        return call_sync(self.request_impl.get_withdraw_history_sapi(coin, status, offset, limit, startTime, endTime))

    def get_withdraw_history(self, asset: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None) -> any:
        """
        Withdraw History (USER_DATA)

        GET /wapi/v3/withdrawHistory.html (HMAC SHA256)

        Fetch withdraw history.
        """
        return call_sync(self.request_impl.get_withdraw_history(asset, status, startTime, endTime))

    def get_deposit_address_sapi(self, coin: 'str', network: 'str' = None) -> any:
        """
        Deposit Address (supporting network) (USER_DATA)

        GET /sapi/v1/capital/deposit/address (HMAC SHA256)

        Fetch deposit address with network.
        """
        return call_sync(self.request_impl.get_deposit_address_sapi(coin, network))

    def get_deposit_address(self, asset: 'str', status: 'boolean' = None) -> any:
        """
        Deposit Address (USER_DATA)

        GET /wapi/v3/depositAddress.html (HMAC SHA256)

        Fetch deposit address with network.
        """
        return call_sync(self.request_impl.get_deposit_address(asset, status))

    def get_account_status(self) -> any:
        """
        Account Status (USER_DATA)

        GET /wapi/v3/accountStatus.html

        Fetch account status detail.
        """
        return call_sync(self.request_impl.get_account_status())

    def get_account_api_trading_status(self) -> any:
        """
        Account API Trading Status (USER_DATA)

        GET /wapi/v3/apiTradingStatus.html

        Fetch account api trading status detail.
        """
        return call_sync(self.request_impl.get_account_api_trading_status())

    def get_dust_log(self) -> any:
        """
        DustLog (USER_DATA)

        GET /wapi/v3/userAssetDribbletLog.html (HMAC SHA256)

        Fetch small amounts of assets exchanged BNB records.
        """
        return call_sync(self.request_impl.get_dust_log())

    def get_trade_fee(self, symbol: str = None) -> any:
        """
        Trade Fee (USER_DATA)

        GET /wapi/v3/tradeFee.html (HMAC SHA256)

        Fetch trade fee.
        """
        return call_sync(self.request_impl.get_trade_fee(symbol))

    def get_asset_detail(self) -> any:
        """
        Asset Detail (USER_DATA)

        GET /wapi/v3/assetDetail.html (HMAC SHA256)

        Fetch asset detail.
        """
        return call_sync(self.request_impl.get_asset_detail())

    def get_sub_account_list(self, email: 'str' = None, status: 'str' = None, page: 'int' = None, limit: 'int' = None) -> any:
        """
        Query Sub-account List(For Master Account)

        GET /wapi/v3/sub-account/list.html (HMAC SHA256)

        Fetch sub account list.
        """
        return call_sync(self.request_impl.get_sub_account_list(email, status, page, limit))

    def get_sub_account_transfer_history(self, email: 'str', startTime: 'int' = None, endTime: 'int' = None, 
                                        page: 'int' = None, limit: 'int' = None) -> any:
        """
        Query Sub-account Transfer History(For Master Account)

        GET /wapi/v3/sub-account/transfer/history.html (HMAC SHA256)

        Fetch transfer history list
        """
        return call_sync(self.request_impl.get_sub_account_transfer_history(email, startTime, endTime, page, limit))

    def post_sub_account_transfer(self, fromEmail: 'str', toEmail: 'str', asset: 'str', amount: 'float') -> any:
        """
        Sub-account Transfer(For Master Account)

        POST /wapi/v3/sub-account/transfer.html (HMAC SHA256)

        Execute sub-account transfer
        """
        return call_sync(self.request_impl.post_sub_account_transfer(fromEmail, toEmail, asset, amount))

    def get_sub_account_assets(self, email: 'str', symbol: 'str' = None) -> any:
        """
        Query Sub-account Assets(For Master Account)

        GET /wapi/v3/sub-account/assets.html (HMAC SHA256)

        Fetch sub-account assets
        """
        return call_sync(self.request_impl.get_sub_account_assets(email, symbol))

    def get_sub_account_deposit_address(self, email: 'str', coin: 'str',  network: 'str' = None) -> any:
        """
        Get Sub-account Deposit Address (For Master Account)

        GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256)

        Fetch sub-account deposit address
        """
        return call_sync(self.request_impl.get_sub_account_deposit_address(email, coin, network))

        
    def get_sub_account_deposit_history(self, email: 'str', coin: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None, offest: 'int' = None) -> any:
        """
        Get Sub-account Deposit History (For Master Account)

        GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256)

        Fetch sub-account deposit history
        """
        return call_sync(self.request_impl.get_sub_account_deposit_history(email, coin, status, startTime, endTime, offest))

        
    def get_sub_account_status(self, email: 'str' = None) -> any:
        """
        Get Sub-account's Status on Margin/Futures(For Master Account)

        GET /sapi/v1/sub-account/status (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_status(email))
        
    def post_sub_account_enable_margin(self, email: 'str' = None) -> any:
        """
        Enable Margin for Sub-account (For Master Account)

        POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)
        """
        return call_sync(self.request_impl.post_sub_account_enable_margin(email))
        
    def get_sub_account_margin_detail(self, email: 'str' = None) -> any:
        """
        Get Detail on Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/margin/account (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_margin_detail(email))
        
    def get_sub_account_margin_summary(self) -> any:
        """
        Get Summary of Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_margin_summary())
         
    def post_sub_account_enable_futures(self, email: 'str' = None) -> any:
        """
        Enable Futures for Sub-account (For Master Account)

        POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)
        """
        return call_sync(self.request_impl.post_sub_account_enable_futures(email)) 

    def get_sub_account_futures_detail(self, email: 'str') -> any:
        """
        Get Detail on Sub-account's Futures Account (For Master Account)

        GET /sapi/v1/sub-account/futures/account (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_futures_detail(email))
           
    def get_sub_account_futures_summary(self) -> any:
        """
        Get Summary of Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_futures_summary())
           
    def get_sub_account_futures_positionrisk(self, email: 'str') -> any:
        """
        Get Futures Postion-Risk of Sub-account (For Master Account)

        GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_sub_account_futures_positionrisk(email))
           
    def post_dust_transfer(self, asset: 'list') -> any:
        """
        Dust Transfer (USER_DATA)

        Post /sapi/v1/asset/dust (HMAC SHA256)

        Convert dust assets to BNB.
        """
        return call_sync(self.request_impl.post_dust_transfer(asset))
           
    def get_asset_dividend_record(self, asset: 'str' = None, startTime: 'long' = None, endTime: 'long' = None) -> any:
        """
        Asset Dividend Record (USER_DATA)

        Get /sapi/v1/asset/assetDividend (HMAC SHA256)

        Query asset dividend record.
        """
        return call_sync(self.request_impl.get_asset_dividend_record(asset, startTime, endTime))
           
    def get_servertime(self) -> any:
        """
        Check Server Time

        GET /api/v3/time

        Test connectivity to the Rest API and get the current server time.
        """
        return call_sync(self.request_impl.get_servertime())
           
    def get_exchange_information(self) -> any:
        """
        Exchange Information

        GET /api/v3/exchangeInfo

        Current exchange trading rules and symbol information
        """
        return call_sync(self.request_impl.get_exchange_information())
           
    def get_order_book(self, symbol: 'str', limit: 'int' = None) -> any:
        """
        Order Book

        GET /api/v3/depth
        """
        return call_sync(self.request_impl.get_order_book(symbol, limit))
           
    def get_recent_trades_list(self, symbol: 'str', limit: 'int' = None) -> any:
        """
        Recent Trades List

        GET /api/v3/trades

        Get recent trades (up to last 500).
        """
        return call_sync(self.request_impl.get_recent_trades_list(symbol, limit))
           
    def get_old_trade_lookup(self, symbol: 'str', limit: 'int' = None, fromId: 'long' = None) -> any:
        """
        Old Trade Lookup

        GET /api/v3/historicalTrades

        Get older market trades.
        """
        return call_sync(self.request_impl.get_old_trade_lookup(symbol, limit, fromId))
           
    def get_aggregate_trades_list(self, symbol: 'str', fromId: 'long' = None, 
                            startTime: 'long' = None, endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        Compressed/Aggregate Trades List

        GET /api/v3/aggTrades

        Get compressed, aggregate trades. Trades that fill at the time, from the same order, 
        with the same price will have the quantity aggregated.
        """
        return call_sync(self.request_impl.get_aggregate_trades_list(symbol, fromId, startTime, endTime, limit))
           
    def get_candlestick_data(self, symbol: 'str', interval: 'CandlestickInterval', 
                            startTime: 'long' = None, endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        Kline/Candlestick Data

        GET /api/v3/klines

        Kline/candlestick bars for a symbol.
        Klines are uniquely identified by their open time.
        """
        return call_sync(self.request_impl.get_candlestick_data(symbol, interval, startTime, endTime, limit))
           
    def get_current_average_price(self, symbol: 'str') -> any:
        """
        Current Average Price

        GET /api/v3/avgPrice

        Current average price for a symbol.
        """
        return call_sync(self.request_impl.get_current_average_price(symbol))
           
    def get_ticker_price_change_statistics(self, symbol: 'str' = None) -> any:
        """
        24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        24 hour rolling window price change statistics. Careful when accessing this with no symbol.
        """
        return call_sync(self.request_impl.get_ticker_price_change_statistics(symbol))
           
    def get_symbol_price_ticker(self, symbol: 'str' = None) -> any:
        """
        Symbol Price Ticker

        GET /api/v3/ticker/price

        Latest price for a symbol or symbols.
        """
        return call_sync(self.request_impl.get_symbol_price_ticker(symbol))
           
    def get_symbol_orderbook_ticker(self, symbol: 'str' = None) -> any:
        """
        Symbol Order Book Ticker

        GET /api/v3/ticker/bookTicker

        Best price/qty on the order book for a symbol or symbols.
        """
        return call_sync(self.request_impl.get_symbol_orderbook_ticker(symbol))

    def post_order(self, symbol: 'str', side: 'OrderSide', ordertype: 'OrderType', 
                timeInForce: 'TimeInForce' = TimeInForce.INVALID, quantity: 'float' = None,
                quoteOrderQty: 'float' = None, price: 'float' = None,
                newClientOrderId: 'str' = None, stopPrice: 'float' = None, icebergQty: 'float' = None,
                newOrderRespType: 'OrderRespType' = OrderRespType.INVALID) -> any:
        """
        New Order (TRADE)

        POST /api/v3/order (HMAC SHA256)

        Send in a new order.
        """
        return call_sync(self.request_impl.post_order(symbol, side, ordertype, 
                timeInForce, quantity,quoteOrderQty, price, newClientOrderId, stopPrice, icebergQty, newOrderRespType))

    def cancel_order(self, symbol: 'str', orderId: 'long' = None, origClientOrderId: 'str' = None, 
                    newClientOrderId: 'str' = None) -> any:
        """
        Cancel Order (TRADE)

        DELETE /api/v3/order (HMAC SHA256)

        Cancel an active order.
        """
        return call_sync(self.request_impl.cancel_order(symbol, orderId, origClientOrderId, newClientOrderId))

    def get_order(self, symbol: 'str', orderId: 'long' = None, origClientOrderId: 'str' = None) -> any:
        """
        Query Order (USER_DATA)

        GET /api/v3/order (HMAC SHA256)

        Check an order's status.
        """
        return call_sync(self.request_impl.get_order(symbol, orderId, origClientOrderId))

    def get_open_orders(self, symbol: 'str' = None) -> any:
        """
        Current Open Orders (USER_DATA)

        GET /api/v3/openOrders (HMAC SHA256)

        Get all open orders on a symbol. Careful when accessing this with no symbol.
        """
        return call_sync(self.request_impl.get_open_orders(symbol))

    def get_all_orders(self, symbol: 'str', orderId: 'long' = None, startTime: 'long' = None, 
                        endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        All Orders (USER_DATA)

        GET /api/v3/allOrders (HMAC SHA256)

        Get all account orders; active, canceled, or filled.
        """
        return call_sync(self.request_impl.get_all_orders(symbol, orderId, startTime, endTime, limit))
    
    def post_oco(self, symbol: 'str', side: 'OrderSide', quantity: 'float', price: 'float', stopPrice: 'float', 
                listClientOrderId: 'str' = None, limitClientOrderId: 'str' = None, limitIcebergQty: 'float' = None,
                stopClientOrderId: 'str' = None, stopLimitPrice: 'float' = None,
                stopIcebergQty: 'float' = None, stopLimitTimeInForce: 'TimeInForce' = TimeInForce.INVALID,
                newOrderRespType: 'OrderRespType' = OrderRespType.INVALID) -> any:
        """
        New OCO (TRADE)

        POST /api/v3/order/oco (HMAC SHA256)

        Send in a new OCO
        """
        return call_sync(self.request_impl.post_oco(symbol, listClientOrderId, side, quantity,
                limitClientOrderId, price, limitIcebergQty, stopClientOrderId, stopPrice, stopLimitPrice,
                stopIcebergQty, stopLimitTimeInForce, newOrderRespType))
    
    def get_open_oco(self) -> any:
        """
        Query Open OCO (USER_DATA)

        GET /api/v3/openOrderList (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_open_oco())
    
    def get_all_oco(self, fromId: 'long' = None, startTime: 'long' = None, 
                        endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        Query all OCO (USER_DATA)

        GET /api/v3/allOrderList (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_all_oco(fromId, startTime, endTime, limit))
    
    def get_oco(self, orderListId: 'long' = None, origClientOrderId: 'str' = None) -> any:
        """
        Query OCO (USER_DATA)

        GET /api/v3/orderList (HMAC SHA256)

        Retrieves a specific OCO based on provided optional parameters
        """
        return call_sync(self.request_impl.get_oco(orderListId, origClientOrderId))
    
    def cancel_oco(self, symbol: 'str', orderListId: 'long' = None, listClientOrderId: 'str' = None, 
                    newClientOrderId: 'str' = None) -> any:
        """
        Cancel OCO (TRADE)

        DELETE /api/v3/orderList (HMAC SHA256)

        Cancel an entire Order List
        """
        return call_sync(self.request_impl.cancel_oco(symbol, orderListId, listClientOrderId, newClientOrderId))
    
    def get_account_information(self) -> any:
        """
        Account Information (USER_DATA)

        GET /api/v3/account (HMAC SHA256)

        Get current account information.
        """
        return call_sync(self.request_impl.get_account_information())
    
    def get_account_trades(self, symbol: 'str', startTime: 'long' = None, endTime: 'long' = None, 
                        fromId: 'long' = None, limit: 'int' = None) -> any:
        """
        Account Trade List (USER_DATA)

        GET /api/v3/myTrades (HMAC SHA256)

        Get trades for a specific account and symbol.
        """
        return call_sync(self.request_impl.get_account_trades(symbol, startTime, endTime, fromId, limit))
    
    def post_margin_transfer(self, asset: 'str', amount: 'float', transferType: 'MarginTransferType') -> any:
        """
        Margin Account Transfer (MARGIN)

        POST /sapi/v1/margin/transfer (HMAC SHA256)

        Execute transfer between spot account and margin account.
        """
        return call_sync(self.request_impl.post_margin_transfer(asset, amount, transferType))
    
    def post_margin_borrow(self, asset: 'str', amount: 'float') -> any:
        """
        Margin Account Borrow (MARGIN)

        POST /sapi/v1/margin/loan (HMAC SHA256)

        Apply for a loan.
        """
        return call_sync(self.request_impl.post_margin_borrow(asset, amount))
    
    def post_margin_repay(self, asset: 'str', amount: 'float') -> any:
        """
        Margin Account Repay (MARGIN)

        POST /sapi/v1/margin/repay (HMAC SHA256)

        Repay loan for margin account.
        """
        return call_sync(self.request_impl.post_margin_repay(asset, amount))
    
    def get_margin_asset(self, asset: 'str') -> any:
        """
        Query Margin Asset (MARKET_DATA)

        GET /sapi/v1/margin/asset
        """
        return call_sync(self.request_impl.get_margin_asset(asset))
    
    def get_margin_pair(self, symbol: 'str') -> any:
        """
        Query Margin Pair (MARKET_DATA)

        GET /sapi/v1/margin/pair
        """
        return call_sync(self.request_impl.get_margin_pair(symbol))
    
    def get_margin_assets(self) -> any:
        """
        Get All Margin Assets (MARKET_DATA)

        GET /sapi/v1/margin/allAssets
        """
        return call_sync(self.request_impl.get_margin_assets())
    
    def get_margin_pairs(self) -> any:
        """
        Get All Margin Pairs (MARKET_DATA)

        GET /sapi/v1/margin/allPairs
        """
        return call_sync(self.request_impl.get_margin_pairs())
    
    def get_margin_priceindex(self, symbol: 'str') -> any:
        """
        Query Margin PriceIndex (MARKET_DATA)

        GET /sapi/v1/margin/priceIndex
        """
        return call_sync(self.request_impl.get_margin_priceindex(symbol))
  
    def post_margin_order(self, symbol: 'str', side: 'OrderSide', ordertype: 'OrderType', 
                quantity: 'float' = None, price: 'float' = None, stopPrice: 'float' = None,
                newClientOrderId: 'str' = None, icebergQty: 'float' = None,
                newOrderRespType: 'OrderRespType' = OrderRespType.INVALID,
                sideEffectType: 'SideEffectType' = SideEffectType.INVALID,
                timeInForce: 'TimeInForce' = TimeInForce.INVALID) -> any:
        """
        Margin Account New Order (TRADE)

        POST /sapi/v1/margin/order (HMAC SHA256) 
        
        Post a new order for margin account.
        """
        return call_sync(self.request_impl.post_margin_order(symbol, side, ordertype, 
                quantity, price, stopPrice, newClientOrderId, icebergQty, newOrderRespType, sideEffectType, timeInForce))

    def cancel_margin_order(self, symbol: 'str', orderId: 'long' = None, origClientOrderId: 'str' = None, 
                    newClientOrderId: 'str' = None) -> any:
        """
        Margin Account Cancel Order (TRADE)

        DELETE /sapi/v1/margin/order (HMAC SHA256) 
        
        Cancel an active order for margin account.
        """
        return call_sync(self.request_impl.cancel_margin_order(symbol, orderId, origClientOrderId, newClientOrderId))

    def get_margin_transfer(self, transferType: 'TransferType', asset: 'str' = None,
                            startTime: 'long' = None, endTime: 'long' = None, 
                            current: 'long' = None, size: 'long' = None) -> any:
        """
        Get Transfer History (USER_DATA)

        GET /sapi/v1/margin/transfer (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_transfer(asset, transferType, startTime, endTime, current, size))

    def get_margin_loan(self, asset: 'str', txId: 'long' = None,
                            startTime: 'long' = None, endTime: 'long' = None, 
                            current: 'long' = None, size: 'long' = None) -> any:
        """
        Query Loan Record (USER_DATA)

        GET /sapi/v1/margin/loan (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_loan(asset, txId, startTime, endTime, current, size))

    def get_margin_repay(self, asset: 'str', txId: 'long' = None,
                            startTime: 'long' = None, endTime: 'long' = None, 
                            current: 'long' = None, size: 'long' = None) -> any:
        """
        Query Repay Record (USER_DATA)

        GET /sapi/v1/margin/repay (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_repay(asset, txId, startTime, endTime, current, size))

    def get_margin_interest(self, asset: 'str' = None,
                            startTime: 'long' = None, endTime: 'long' = None, 
                            current: 'long' = None, size: 'long' = None) -> any:
        """
        Get Interest History (USER_DATA)

        GET /sapi/v1/margin/interestHistory (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_interest(asset, startTime, endTime, current, size))

    def get_margin_force_liquidation(self, startTime: 'long' = None, endTime: 'long' = None, 
                            current: 'long' = None, size: 'long' = None) -> any:
        """
        Get Force Liquidation Record (USER_DATA)

        GET /sapi/v1/margin/forceLiquidationRec (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_force_liquidation(startTime, endTime, current, size))

    def get_margin_account(self) -> any:
        """
        Query Margin Account Details (USER_DATA)

        GET /sapi/v1/margin/account (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_account())

    def get_margin_order(self, symbol: 'str', orderId: 'str' = None, origClientOrderId: 'str' = None) -> any:
        """
        Query Margin Account's Order (USER_DATA)

        GET /sapi/v1/margin/order (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_order(symbol, orderId, origClientOrderId))

    def get_margin_open_orders(self, symbol: 'str' = None) -> any:
        """
        Query Margin Account's Open Order (USER_DATA)

        GET /sapi/v1/margin/openOrders (HMAC SHA256)
        """
        return call_sync(self.request_impl.get_margin_open_orders(symbol))