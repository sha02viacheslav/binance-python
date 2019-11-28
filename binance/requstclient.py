from binance.constant.system import RestApiDefine
from binance.impl.restapirequestimpl import RestApiRequestImpl
from binance.impl.restapiinvoker import call_sync


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