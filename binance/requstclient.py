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

    def system_status(self) -> any:
        """
        System status (System)
        
        GET /wapi/v3/systemStatus.html

        Get the system status.
        """
        return call_sync(self.request_impl.system_status())

    def all_coins_information(self) -> any:
        """
        All Coins' Information (USER_DATA)

        GET /sapi/v1/capital/config/getall (HMAC SHA256)

        Get all coins' information for user.
        """
        return call_sync(self.request_impl.all_coins_information())

    def withdraw_sapi(self, coin: 'str', address: 'str', amount: 'float', network: 'str' = None, 
                        addressTag: 'str' = None, name: 'str' = None) -> str:
        """
        Withdraw [SAPI]

        POST /sapi/v1/capital/withdraw/apply (HMAC SHA256)

        Submit a withdraw request.
        """
        return call_sync(self.request_impl.withdraw_sapi(coin, address, amount, network, addressTag, name))

    def withdraw(self, asset: 'str', address: 'str', amount: 'float', network: 'str' = None, 
                        addressTag: 'str' = None, name: 'str' = None) -> str:
        """
        Withdraw

        POST /wapi/v3/withdraw.html (HMAC SHA256)

        Submit a withdraw request.
        """
        return call_sync(self.request_impl.withdraw(asset, address, amount, network, addressTag, name))

    def deposit_history_sapi(self, coin: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None, offest: 'int' = None) -> any:
        """
        Deposit History（supporting network） (USER_DATA)

        GET /sapi/v1/capital/deposit/hisrec (HMAC SHA256)

        Fetch deposit history.
        """
        return call_sync(self.request_impl.deposit_history_sapi(coin, status, startTime, endTime, offest))

    def deposit_history(self, asset: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None) -> any:
        """
        Deposit History (USER_DATA)

        GET /wapi/v3/depositHistory.html (HMAC SHA256)

        Fetch deposit history.
        """
        return call_sync(self.request_impl.deposit_history(asset, status, startTime, endTime))
    
    def withdraw_history_sapi(self, coin: 'str' = None, status: 'int' = None, offset: 'int' = None, limit: 'int' = None, 
                                startTime: 'long' = None, endTime: 'long' = None) -> any:
        """
        Withdraw History (supporting network) (USER_DATA)

        Get /sapi/v1/capital/withdraw/history (HMAC SHA256)

        Fetch withdraw history.
        """
        return call_sync(self.request_impl.withdraw_history_sapi(coin, status, offset, limit, startTime, endTime))

    def withdraw_history(self, asset: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None) -> any:
        """
        Withdraw History (USER_DATA)

        GET /wapi/v3/withdrawHistory.html (HMAC SHA256)

        Fetch withdraw history.
        """
        return call_sync(self.request_impl.withdraw_history(asset, status, startTime, endTime))

    def deposit_address_sapi(self, coin: 'str', network: 'str' = None) -> any:
        """
        Deposit Address (supporting network) (USER_DATA)

        GET /sapi/v1/capital/deposit/address (HMAC SHA256)

        Fetch deposit address with network.
        """
        return call_sync(self.request_impl.deposit_address_sapi(coin, network))

    def deposit_address(self, asset: 'str', status: 'boolean' = None) -> any:
        """
        Deposit Address (USER_DATA)

        GET /wapi/v3/depositAddress.html (HMAC SHA256)

        Fetch deposit address with network.
        """
        return call_sync(self.request_impl.deposit_address(asset, status))

    def account_status(self) -> any:
        """
        Account Status (USER_DATA)

        GET /wapi/v3/accountStatus.html

        Fetch account status detail.
        """
        return call_sync(self.request_impl.account_status())

    def account_api_trading_status(self) -> any:
        """
        Account API Trading Status (USER_DATA)

        GET /wapi/v3/apiTradingStatus.html

        Fetch account api trading status detail.
        """
        return call_sync(self.request_impl.account_api_trading_status())

    def dust_log(self) -> any:
        """
        DustLog (USER_DATA)

        GET /wapi/v3/userAssetDribbletLog.html (HMAC SHA256)

        Fetch small amounts of assets exchanged BNB records.
        """
        return call_sync(self.request_impl.dust_log())

    def trade_fee(self, symbol: str = None) -> any:
        """
        Trade Fee (USER_DATA)

        GET /wapi/v3/tradeFee.html (HMAC SHA256)

        Fetch trade fee.
        """
        return call_sync(self.request_impl.trade_fee(symbol))

    def asset_detail(self) -> any:
        """
        Asset Detail (USER_DATA)

        GET /wapi/v3/assetDetail.html (HMAC SHA256)

        Fetch asset detail.
        """
        return call_sync(self.request_impl.asset_detail())

    def sub_account_list(self, email: 'str' = None, status: 'str' = None, page: 'int' = None, limit: 'int' = None) -> any:
        """
        Query Sub-account List(For Master Account)

        GET /wapi/v3/sub-account/list.html (HMAC SHA256)

        Fetch sub account list.
        """
        return call_sync(self.request_impl.sub_account_list(email, status, page, limit))

    def sub_account_transfer_history(self, email: 'str', startTime: 'int' = None, endTime: 'int' = None, 
                                        page: 'int' = None, limit: 'int' = None) -> any:
        """
        Query Sub-account Transfer History(For Master Account)

        GET /wapi/v3/sub-account/transfer/history.html (HMAC SHA256)

        Fetch transfer history list
        """
        return call_sync(self.request_impl.sub_account_transfer_history(email, startTime, endTime, page, limit))

    def sub_account_transfer(self, fromEmail: 'str', toEmail: 'str', asset: 'str', amount: 'float') -> any:
        """
        Sub-account Transfer(For Master Account)

        POST /wapi/v3/sub-account/transfer.html (HMAC SHA256)

        Execute sub-account transfer
        """
        return call_sync(self.request_impl.sub_account_transfer(fromEmail, toEmail, asset, amount))

    def sub_account_assets(self, email: 'str', symbol: 'str' = None) -> any:
        """
        Query Sub-account Assets(For Master Account)

        GET /wapi/v3/sub-account/assets.html (HMAC SHA256)

        Fetch sub-account assets
        """
        return call_sync(self.request_impl.sub_account_assets(email, symbol))

    def sub_account_deposit_address(self, email: 'str', coin: 'str',  network: 'str' = None) -> any:
        """
        Get Sub-account Deposit Address (For Master Account)

        GET /sapi/v1/capital/deposit/subAddress (HMAC SHA256)

        Fetch sub-account deposit address
        """
        return call_sync(self.request_impl.sub_account_deposit_address(email, coin, network))

        
    def sub_account_deposit_history(self, email: 'str', coin: 'str' = None, status: 'int' = None, startTime: 'long' = None, 
                                endTime: 'long' = None, offest: 'int' = None) -> any:
        """
        Get Sub-account Deposit History (For Master Account)

        GET /sapi/v1/capital/deposit/subHisrec (HMAC SHA256)

        Fetch sub-account deposit history
        """
        return call_sync(self.request_impl.sub_account_deposit_history(email, coin, status, startTime, endTime, offest))

        
    def sub_account_status(self, email: 'str' = None) -> any:
        """
        Get Sub-account's Status on Margin/Futures(For Master Account)

        GET /sapi/v1/sub-account/status (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_status(email))
        
    def sub_account_enable_margin(self, email: 'str' = None) -> any:
        """
        Enable Margin for Sub-account (For Master Account)

        POST /sapi/v1/sub-account/margin/enable (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_enable_margin(email))
        
    def sub_account_margin_detail(self, email: 'str' = None) -> any:
        """
        Get Detail on Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/margin/account (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_margin_detail(email))
        
    def sub_account_margin_summary(self) -> any:
        """
        Get Summary of Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/margin/accountSummary (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_margin_summary())
         
    def sub_account_enable_futures(self, email: 'str' = None) -> any:
        """
        Enable Futures for Sub-account (For Master Account)

        POST /sapi/v1/sub-account/futures/enable (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_enable_futures(email)) 

    def sub_account_futures_detail(self, email: 'str') -> any:
        """
        Get Detail on Sub-account's Futures Account (For Master Account)

        GET /sapi/v1/sub-account/futures/account (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_futures_detail(email))
           
    def sub_account_futures_summary(self) -> any:
        """
        Get Summary of Sub-account's Margin Account (For Master Account)

        GET /sapi/v1/sub-account/futures/accountSummary (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_futures_summary())
           
    def sub_account_futures_positionrisk(self, email: 'str') -> any:
        """
        Get Futures Postion-Risk of Sub-account (For Master Account)

        GET /sapi/v1/sub-account/futures/positionRisk (HMAC SHA256)
        """
        return call_sync(self.request_impl.sub_account_futures_positionrisk(email))
           
    def dust_transfer(self, asset: 'list') -> any:
        """
        Dust Transfer (USER_DATA)

        Post /sapi/v1/asset/dust (HMAC SHA256)

        Convert dust assets to BNB.
        """
        return call_sync(self.request_impl.dust_transfer(asset))
           
    def asset_dividend_record(self, asset: 'str' = None, startTime: 'long' = None, endTime: 'long' = None) -> any:
        """
        Asset Dividend Record (USER_DATA)

        Get /sapi/v1/asset/assetDividend (HMAC SHA256)

        Query asset dividend record.
        """
        return call_sync(self.request_impl.asset_dividend_record(asset, startTime, endTime))
           
    def check_servertime(self) -> any:
        """
        Check Server Time

        GET /api/v3/time

        Test connectivity to the Rest API and get the current server time.
        """
        return call_sync(self.request_impl.check_servertime())
           
    def exchange_information(self) -> any:
        """
        Exchange Information

        GET /api/v3/exchangeInfo

        Current exchange trading rules and symbol information
        """
        return call_sync(self.request_impl.exchange_information())
           
    def order_book(self, symbol: 'str', limit: 'int' = None) -> any:
        """
        Order Book

        GET /api/v3/depth
        """
        return call_sync(self.request_impl.order_book(symbol, limit))
           
    def recent_trades_list(self, symbol: 'str', limit: 'int' = None) -> any:
        """
        Recent Trades List

        GET /api/v3/trades

        Get recent trades (up to last 500).
        """
        return call_sync(self.request_impl.recent_trades_list(symbol, limit))
           
    def old_trade_lookup(self, symbol: 'str', limit: 'int' = None, fromId: 'long' = None) -> any:
        """
        Old Trade Lookup

        GET /api/v3/historicalTrades

        Get older market trades.
        """
        return call_sync(self.request_impl.old_trade_lookup(symbol, limit, fromId))
           
    def aggregate_trades_list(self, symbol: 'str', fromId: 'long' = None, 
                            startTime: 'long' = None, endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        Compressed/Aggregate Trades List

        GET /api/v3/aggTrades

        Get compressed, aggregate trades. Trades that fill at the time, from the same order, 
        with the same price will have the quantity aggregated.
        """
        return call_sync(self.request_impl.aggregate_trades_list(symbol, fromId, startTime, endTime, limit))
           
    def candlestick_data(self, symbol: 'str', interval: 'CandlestickInterval', 
                            startTime: 'long' = None, endTime: 'long' = None, limit: 'int' = None) -> any:
        """
        Kline/Candlestick Data

        GET /api/v3/klines

        Kline/candlestick bars for a symbol.
        Klines are uniquely identified by their open time.
        """
        return call_sync(self.request_impl.candlestick_data(symbol, interval, startTime, endTime, limit))
           
    def current_average_price(self, symbol: 'str') -> any:
        """
        Current Average Price

        GET /api/v3/avgPrice

        Current average price for a symbol.
        """
        return call_sync(self.request_impl.current_average_price(symbol))
           
    def ticker_price_change_statistics(self, symbol: 'str' = None) -> any:
        """
        24hr Ticker Price Change Statistics

        GET /api/v3/ticker/24hr

        24 hour rolling window price change statistics. Careful when accessing this with no symbol.
        """
        return call_sync(self.request_impl.ticker_price_change_statistics(symbol))
           
    def symbol_price_ticker(self, symbol: 'str' = None) -> any:
        """
        Symbol Price Ticker

        GET /api/v3/ticker/price

        Latest price for a symbol or symbols.
        """
        return call_sync(self.request_impl.symbol_price_ticker(symbol))
