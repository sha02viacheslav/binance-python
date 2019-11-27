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