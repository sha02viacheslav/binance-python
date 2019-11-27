from binance.impl import RestApiRequest
from binance.impl.utils.urlparamsbuilder import UrlParamsBuilder
from binance.impl.utils.apisignature import create_signature
from binance.impl.utils.inputchecker import *
from binance.impl.utils.timeservice import *
from binance.model import *
# For develop
from binance.base.printobject import *


class RestApiRequestImpl(object):

    def __init__(self, api_key, secret_key, server_url="https://api.binance.com"):
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__server_url = server_url

    def __create_request_by_get(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        create_signature(self.__secret_key, builder)
        request.header.update({'Content-Type': 'application/json'})
        request.post_body = builder.post_map
        request.url = url + builder.build_url()
        return request

    def __create_request_by_get_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        builder.put_url("recvWindow", 60000)
        builder.put_url("timestamp", str(get_current_timestamp()))
        create_signature(self.__secret_key, builder)
        request.header.update({"Content-Type": "application/x-www-form-urlencoded"})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
        request.url = url + builder.build_url()
        # For develop
        print("====== Request ======")
        print(request)
        PrintMix.print_data(request)
        print("=====================")
        return request

    def system_status(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get("/wapi/v3/systemStatus.html", builder)

        def parse(json_wrapper):
            trade_statistics = SystemStatus()
            trade_statistics.status = json_wrapper.get_string("status")
            trade_statistics.msg = json_wrapper.get_string("msg")
            return trade_statistics

        request.json_parser = parse
        return request

    def all_coins_information(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/config/getall", builder)

        def parse(json_wrapper):
            all_coins_information = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                coin_information = CoinInformation.json_parse(item)
                all_coins_information.append(coin_information)
            return all_coins_information

        request.json_parser = parse
        return request