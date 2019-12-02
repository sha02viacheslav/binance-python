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

    def deposit_address(self, asset, status):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("status", status)

        request = self.__create_request_by_get_with_signature("/wapi/v3/depositAddress.html", builder)

        def parse(json_wrapper):
            deposit_address = DepositAddress.json_parse(json_wrapper)
            return deposit_address

        request.json_parser = parse
        return request

    def account_status(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/accountStatus.html", builder)

        def parse(json_wrapper):
            account_status = AccountStatus()
            account_status.msg = json_wrapper.get_string("msg")
            if(json_wrapper.contain_key("objs")):
                account_status.objs = json_wrapper.get_array("objs")
            return account_status

        request.json_parser = parse
        return request

    def account_api_trading_status(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/apiTradingStatus.html", builder)

        def parse(json_wrapper):
            account_api_trading_status = AccountApiTradingStatus.json_parse(json_wrapper.get_object("status"))
            return account_api_trading_status

        request.json_parser = parse
        return request

    def dust_log(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/userAssetDribbletLog.html", builder)

        def parse(json_wrapper):
            dust_logs = DustLogs.json_parse(json_wrapper.get_object("results"))
            return dust_logs

        request.json_parser = parse
        return request

    def trade_fee(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_signature("/wapi/v3/tradeFee.html", builder)

        def parse(json_wrapper):
            trade_fee_list = list()
            data_list = json_wrapper.get_array("tradeFee")
            for item in data_list.get_items():
                trade_fee = TradeFee.json_parse(item)
                trade_fee_list.append(trade_fee)
            return trade_fee_list

        request.json_parser = parse
        return request

    def asset_detail(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/assetDetail.html", builder)

        def parse(json_wrapper):
            asset_detail_list = list()
            data_list = json_wrapper.get_array("assetDetail")
            for item in data_list.get_items():
                asset_detail = AssetDetail()
                asset_detail.asset = item.json_object
                json_data = data_list.get_object_at(asset_detail.asset)
                asset_detail.minWithdrawAmount = json_data.get_float("minWithdrawAmount")
                asset_detail.depositStatus = json_data.get_boolean("depositStatus")
                asset_detail.withdrawFee = json_data.get_float("withdrawFee")
                asset_detail.withdrawStatus = json_data.get_boolean("withdrawStatus")
                asset_detail.depositTip = json_data.get_string_or_default("depositTip", "")
                asset_detail_list.append(asset_detail)
            return asset_detail_list

        request.json_parser = parse
        return request

    def sub_account_list(self, email, status, page, limit):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)
        builder.put_url("status", status)
        builder.put_url("page", page)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/wapi/v3/sub-account/list.html", builder)

        def parse(json_wrapper):
            sub_account_list = list()
            data_list = json_wrapper.get_array("subAccounts")
            for item in data_list.get_items():
                sub_account = SubAccount().json_parse(item)
                sub_account_list.append(sub_account)
            return sub_account_list

        request.json_parser = parse
        return request

    def sub_account_transfer_history(self, email, startTime, endTime, page, limit):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("page", page)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/wapi/v3/sub-account/transfer/history.html", builder)

        def parse(json_wrapper):
            sub_account_transfer_history = list()
            data_list = json_wrapper.get_array("transfers")
            for item in data_list.get_items():
                sub_account_transfer = SubAccountTransfer().json_parse(item)
                sub_account_transfer_history.append(sub_account_transfer)
            return sub_account_transfer_history

        request.json_parser = parse
        return request

    def sub_account_transfer(self, fromEmail, toEmail, asset, amount):
        check_should_not_none(fromEmail, "fromEmail")
        check_should_not_none(toEmail, "toEmail")
        check_should_not_none(asset, "asset")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_url("fromEmail", fromEmail)
        builder.put_url("toEmail", toEmail)
        builder.put_url("asset", asset)
        builder.put_url("amount", amount)

        request = self.__create_request_by_post_with_signature("/wapi/v3/sub-account/transfer.html", builder)

        def parse(json_wrapper):
            txnId = json_wrapper.get_string("txnId")
            return txnId

        request.json_parser = parse
        return request

    def sub_account_assets(self, email, symbol):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_signature("/wapi/v3/sub-account/assets.html", builder)

        def parse(json_wrapper):
            sub_account_asset_list = list()
            data_list = json_wrapper.get_array("balances")
            for item in data_list.get_items():
                sub_account_asset = SubAccountAsset().json_parse(item)
                sub_account_asset_list.append(sub_account_asset)
            return sub_account_asset_list


        request.json_parser = parse
        return request

    def sub_account_deposit_address(self, email, coin, network):
        check_should_not_none(email, "email")
        check_should_not_none(coin, "coin")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)
        builder.put_url("coin", coin)
        builder.put_url("network", network)

        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/deposit/subAddress", builder)

        def parse(json_wrapper):
            sub_account_deposit_address = DepositAddressSapi.json_parse(json_wrapper)
            return sub_account_deposit_address


        request.json_parser = parse
        return request

        
    def sub_account_deposit_history(self, email, coin, status, startTime, endTime, offest):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)
        builder.put_url("coin", coin)
        builder.put_url("status", status)
        builder.put_url("status", status)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("offest", offest)

        request = self.__create_request_by_get_with_signature("/sapi/v1/capital/deposit/subHisrec", builder)

        def parse(json_wrapper):
            deposit_historys = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                deposit_history = SubAccountDepositHistory.json_parse(item)
                deposit_historys.append(deposit_history)
            return deposit_historys

        request.json_parser = parse
        return request
