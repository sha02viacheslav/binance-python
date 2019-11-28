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
        builder.put_url("recvWindow", 60000)
        builder.put_url("timestamp", str(get_current_timestamp()))
        create_signature(self.__secret_key, builder)
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
        request.post_body = builder.post_map
        request.url = url + builder.build_url()
        # For develop
        print("====== Request ======")
        print(request)
        PrintMix.print_data(request)
        print("=====================")
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
        
    def withdraw_sapi(self, coin, address, amount, network, addressTag, name):
        check_should_not_none(coin, "coin")
        check_should_not_none(address, "address")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_url("coin", coin)
        builder.put_url("address", address)
        builder.put_url("amount", amount)
        builder.put_url("network", network)
        builder.put_url("addressTag", addressTag)
        builder.put_url("name", name)

        request = self.__create_request_by_post_with_signature("/sapi/v1/capital/withdraw/apply", builder)

        def parse(json_wrapper):
            return json_wrapper.get_string_or_default("id", "")

        request.json_parser = parse
        return request
        
    def withdraw(self, asset, address, amount, network, addressTag, name):
        check_should_not_none(asset, "asset")
        check_should_not_none(address, "address")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("address", address)
        builder.put_url("amount", amount)
        builder.put_url("network", network)
        builder.put_url("addressTag", addressTag)
        builder.put_url("name", name)

        request = self.__create_request_by_post_with_signature("/wapi/v3/withdraw.html", builder)

        def parse(json_wrapper):
            return json_wrapper.get_string_or_default("id", "")

        request.json_parser = parse
        return request

    def deposit_history_sapi(self, coin, status, startTime, endTime, offest):
        builder = UrlParamsBuilder()
        builder.put_url("coin", coin)
        builder.put_url("status", status)
        builder.put_url("status", status)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("offest", offest)

        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/deposit/hisrec", builder)

        def parse(json_wrapper):
            deposit_historys = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                deposit_history = DepositHistorySapi.json_parse(item)
                deposit_historys.append(deposit_history)
            PrintMix.print_data(deposit_historys)
            return deposit_historys

        request.json_parser = parse
        return request

    def deposit_history(self, asset, status, startTime, endTime):
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("status", status)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)

        request = self.__create_request_by_get_with_signature("/wapi/v3/depositHistory.html", builder)

        def parse(json_wrapper):
            deposit_historys = list()
            data_list = json_wrapper.get_array("depositList")
            for item in data_list.get_items():
                deposit_history = DepositHistory.json_parse(item)
                deposit_historys.append(deposit_history)
            PrintMix.print_data(deposit_historys)
            return deposit_historys

        request.json_parser = parse
        return request
   
    def withdraw_history_sapi(self, coin, status, offest, limit, startTime, endTime):
        builder = UrlParamsBuilder()
        builder.put_url("coin", coin)
        builder.put_url("status", status)
        builder.put_url("offest", offest)
        builder.put_url("limit", limit)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)

        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/withdraw/history", builder)

        def parse(json_wrapper):
            withdraw_historys = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                withdraw_history = WithdrawHistorySapi.json_parse(item)
                withdraw_historys.append(withdraw_history)
            PrintMix.print_data(withdraw_historys)
            return withdraw_historys

        request.json_parser = parse
        return request

    def withdraw_history(self, asset, status, startTime, endTime):
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("status", status)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)

        request = self.__create_request_by_get_with_signature("/wapi/v3/withdrawHistory.html", builder)

        def parse(json_wrapper):
            withdraw_historys = list()
            data_list = json_wrapper.get_array("withdrawList")
            for item in data_list.get_items():
                withdraw_history = DepositHistory.json_parse(item)
                withdraw_historys.append(withdraw_history)
            return withdraw_historys

        request.json_parser = parse
        return request

    def deposit_address_sapi(self, coin, network):
        check_should_not_none(coin, "coin")
        builder = UrlParamsBuilder()
        builder.put_url("coin", coin)
        builder.put_url("network", network)

        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/deposit/address", builder)

        def parse(json_wrapper):
            deposit_address = DepositAddressSapi.json_parse(json_wrapper)
            return deposit_address

        request.json_parser = parse
        return request