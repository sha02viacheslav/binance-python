from binance.impl import RestApiRequest
from binance.impl.utils.urlparamsbuilder import UrlParamsBuilder
from binance.impl.utils.apisignature import create_signature
from binance.impl.utils.apisignature import create_signature_with_query
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

    def __create_request_by_get_with_apikey(self, url, builder):
        request = RestApiRequest()
        request.method = "GET"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
        request.url = url + builder.build_url()
        return request

    def __create_request_by_post_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        builder.put_url("recvWindow", 60000)
        builder.put_url("timestamp", str(get_current_timestamp() - 1000))
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

    def __create_request_by_post_with_apikey(self, url, builder):
        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
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

    def __create_request_by_delete_with_signature(self, url, builder):
        request = RestApiRequest()
        request.method = "DELETE"
        request.host = self.__server_url
        builder.put_url("recvWindow", 60000)
        builder.put_url("timestamp", str(get_current_timestamp() - 1000))
        create_signature(self.__secret_key, builder)
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
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
        builder.put_url("timestamp", str(get_current_timestamp() - 1000))
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

    def __create_request_by_put_with_apikey(self, url, builder):
        request = RestApiRequest()
        request.method = "PUT"
        request.host = self.__server_url
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
        request.url = url + builder.build_url()
        # For develop
        print("====== Request ======")
        print(request)
        PrintMix.print_data(request)
        print("=====================")
        return request

    def get_system_status(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get("/wapi/v3/systemStatus.html", builder)

        def parse(json_wrapper):
            trade_statistics = SystemStatus()
            trade_statistics.status = json_wrapper.get_string("status")
            trade_statistics.msg = json_wrapper.get_string("msg")
            return trade_statistics

        request.json_parser = parse
        return request

    def get_all_coins_information(self):
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
        
    def post_withdraw_sapi(self, coin, address, amount, network, addressTag, name):
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
        
    def post_withdraw(self, asset, address, amount, network, addressTag, name):
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

    def get_deposit_history_sapi(self, coin, status, startTime, endTime, offest):
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

    def get_deposit_history(self, asset, status, startTime, endTime):
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
   
    def get_withdraw_history_sapi(self, coin, status, offest, limit, startTime, endTime):
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

    def get_withdraw_history(self, asset, status, startTime, endTime):
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

    def get_deposit_address_sapi(self, coin, network):
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

    def get_deposit_address(self, asset, status):
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

    def get_account_status(self):
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

    def get_account_api_trading_status(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/apiTradingStatus.html", builder)

        def parse(json_wrapper):
            account_api_trading_status = AccountApiTradingStatus.json_parse(json_wrapper.get_object("status"))
            return account_api_trading_status

        request.json_parser = parse
        return request

    def get_dust_log(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/wapi/v3/userAssetDribbletLog.html", builder)

        def parse(json_wrapper):
            dust_logs = DustLogs.json_parse(json_wrapper.get_object("results"))
            return dust_logs

        request.json_parser = parse
        return request

    def get_trade_fee(self, symbol):
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

    def get_asset_detail(self):
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

    def get_sub_account_list(self, email, status, page, limit):
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

    def get_sub_account_transfer_history(self, email, startTime, endTime, page, limit):
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

    def post_sub_account_transfer(self, fromEmail, toEmail, asset, amount):
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

    def get_sub_account_assets(self, email, symbol):
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

    def get_sub_account_deposit_address(self, email, coin, network):
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

        
    def get_sub_account_deposit_history(self, email, coin, status, startTime, endTime, offest):
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
        
    def get_sub_account_status(self, email):
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/status", builder)

        def parse(json_wrapper):
            sub_account_status_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                sub_accouont_status = SubAccountStatus.json_parse(item)
                sub_account_status_list.append(sub_accouont_status)
            return sub_account_status_list

        request.json_parser = parse
        return request
        
    def post_sub_account_enable_margin(self, email):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_post_with_signature("/sapi/v1/sub-account/margin/enable", builder)

        def parse(json_wrapper):
            if json_wrapper.contain_key("isMarginEnabled"):
                isMarginEnabled = json_wrapper.get_string("isMarginEnabled")
                if isMarginEnabled == "true":
                    margin_email = json_wrapper.get_string("email")
                    return margin_email
            return None

        request.json_parser = parse
        return request
        
    def get_sub_account_margin_detail(self, email):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/margin/account", builder)

        def parse(json_wrapper):
            sub_account_margin_detail = SubAccountMarginDetail.json_parse(json_wrapper)
            return sub_account_margin_detail

        request.json_parser = parse
        return request
        
    def get_sub_account_margin_summary(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/margin/accountSummary", builder)

        def parse(json_wrapper):
            sub_account_margin_summary = SubAccountMarginSummary.json_parse(json_wrapper)
            return sub_account_margin_summary

        request.json_parser = parse
        return request
      
    def post_sub_account_enable_futures(self, email):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_post_with_signature("/sapi/v1/sub-account/futures/enable", builder)

        def parse(json_wrapper):
            if json_wrapper.contain_key("isFuturesEnabled"):
                isFuturesEnabled = json_wrapper.get_string("isFuturesEnabled")
                if isFuturesEnabled == "true":
                    futures_email = json_wrapper.get_string("email")
                    return futures_email
            return None

        request.json_parser = parse
        return request
                
    def get_sub_account_futures_detail(self, email):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/futures/account", builder)

        def parse(json_wrapper):
            sub_account_futures_detail = SubAccountFuturesDetail.json_parse(json_wrapper)
            return sub_account_futures_detail

        request.json_parser = parse
        return request
                
    def get_sub_account_futures_summary(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/futures/accountSummary", builder)

        def parse(json_wrapper):
            sub_account_futures_summary = SubAccountFuturesSummary.json_parse(json_wrapper)
            return sub_account_futures_summary

        request.json_parser = parse
        return request
                
    def get_sub_account_futures_positionrisk(self, email):
        check_should_not_none(email, "email")
        builder = UrlParamsBuilder()
        builder.put_url("email", email)

        request = self.__create_request_by_get_with_signature("/sapi/v1/sub-account/futures/positionRisk", builder)

        def parse(json_wrapper):
            sub_account_futures_positionrisk_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                sub_account_futures_positionrisk = SubAccountFuturesPositionrisk.json_parse(item)
                sub_account_futures_positionrisk_list.append(sub_account_futures_positionrisk)
            return sub_account_futures_positionrisk_list

        request.json_parser = parse
        return request

    def post_dust_transfer(self, asset):
        check_should_not_none(asset, "asset")
        query_string = "recvWindow=60000"
        query_string += "&timestamp=" + str(get_current_timestamp())
        for item in asset:
            query_string += "&asset=" + item

        request = RestApiRequest()
        request.method = "POST"
        request.host = self.__server_url
        signature = create_signature_with_query(self.__secret_key, query_string)
        query_string += "&signature=" + signature
        request.header.update({'Content-Type': 'application/json'})
        request.header.update({"X-MBX-APIKEY": self.__api_key})
        request.url = "/sapi/v1/asset/dust?" + query_string
        # For develop
        print("====== Request ======")
        print(request)
        PrintMix.print_data(request)
        print("=====================")

        def parse(json_wrapper):
            dust_transfer = DustTransfer.json_parse(json_wrapper)
            return dust_transfer

        request.json_parser = parse
        return request

    def get_asset_dividend_record(self, asset, startTime, endTime):
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)

        request = self.__create_request_by_get_with_signature("/sapi/v1/asset/assetDividend", builder)

        def parse(json_wrapper):
            asset_dividend_record = AssetDividendRecord.json_parse(json_wrapper)
            return asset_dividend_record

        request.json_parser = parse
        return request
        
    def get_servertime(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get("/api/v3/time", builder)

        def parse(json_wrapper):
            server_time = json_wrapper.get_int("serverTime")
            return server_time

        request.json_parser = parse
        return request
        
    def get_exchange_information(self):
        builder = UrlParamsBuilder()
        request = self.__create_request_by_get("/api/v3/exchangeInfo", builder)

        def parse(json_wrapper):
            exchange_information = ExchangeInformation.json_parse(json_wrapper)
            return exchange_information

        request.json_parser = parse
        return request
            
    def get_order_book(self, symbol, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get("/api/v3/depth", builder)

        def parse(json_wrapper):
            order_book = OrderBook.json_parse(json_wrapper)
            return order_book

        request.json_parser = parse
        return request
      
    def get_recent_trades_list(self, symbol, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get("/api/v3/trades", builder)

        def parse(json_wrapper):
            recent_trade_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                trade = Trade.json_parse(item)
                recent_trade_list.append(trade)
            return recent_trade_list

        request.json_parser = parse
        return request
      
    def get_old_trade_lookup(self, symbol, limit, fromId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("limit", limit)
        builder.put_url("fromId", fromId)

        request = self.__create_request_by_get_with_apikey("/api/v3/historicalTrades", builder)

        def parse(json_wrapper):
            old_trade_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                trade = Trade.json_parse(item)
                old_trade_list.append(trade)
            return old_trade_list

        request.json_parser = parse
        return request
      
    def get_aggregate_trades_list(self, symbol, fromId, startTime, endTime, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("fromId", fromId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get("/api/v3/aggTrades", builder)

        def parse(json_wrapper):
            aggregate_trades_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                trade = AggregateTrade.json_parse(item)
                aggregate_trades_list.append(trade)
            return aggregate_trades_list

        request.json_parser = parse
        return request
      
    def get_candlestick_data(self, symbol, interval, startTime, endTime, limit):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(symbol, "interval")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("interval", interval)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get("/api/v3/klines", builder)

        def parse(json_wrapper):
            candlestick_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                candlestick = Candlestick.json_parse(item)
                candlestick_list.append(candlestick)
            return candlestick_list

        request.json_parser = parse
        return request
      
    def get_current_average_price(self, symbol):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get("/api/v3/avgPrice", builder)

        def parse(json_wrapper):
            current_average_price = AveragePrice.json_parse(json_wrapper)
           
            return current_average_price

        request.json_parser = parse
        return request
      
    def get_ticker_price_change_statistics(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get("/api/v3/ticker/24hr", builder)

        def parse(json_wrapper):
            ticker_price_change_statistics = list()

            if symbol:
                information = TickerPriceChangeStatistics.json_parse(json_wrapper)
                ticker_price_change_statistics.append(information)
            else:
                data_list = json_wrapper.convert_2_array()
                for item in data_list.get_items():
                    information = TickerPriceChangeStatistics.json_parse(item)
                    ticker_price_change_statistics.append(information)

            return ticker_price_change_statistics

        request.json_parser = parse
        return request
      
    def get_symbol_price_ticker(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get("/api/v3/ticker/price", builder)

        def parse(json_wrapper):
            symbol_price_list = list()

            if symbol:
                information = SymbolPrice.json_parse(json_wrapper)
                symbol_price_list.append(information)
            else:
                data_list = json_wrapper.convert_2_array()
                for item in data_list.get_items():
                    information = SymbolPrice.json_parse(item)
                    symbol_price_list.append(information)

            return symbol_price_list

        request.json_parser = parse
        return request
      
    def get_symbol_orderbook_ticker(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get("/api/v3/ticker/bookTicker", builder)

        def parse(json_wrapper):
            symbol_orderbook_list = list()

            if symbol:
                information = SymbolOrderbook.json_parse(json_wrapper)
                symbol_orderbook_list.append(information)
            else:
                data_list = json_wrapper.convert_2_array()
                for item in data_list.get_items():
                    information = SymbolOrderbook.json_parse(item)
                    symbol_orderbook_list.append(information)

            return symbol_orderbook_list

        request.json_parser = parse
        return request
      
    def post_order(self, symbol, side, ordertype, 
                timeInForce, quantity, quoteOrderQty, price, newClientOrderId, stopPrice, icebergQty, newOrderRespType):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(side, "side")
        check_should_not_none(ordertype, "ordertype")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("side", side)
        builder.put_url("type", ordertype)
        builder.put_url("timeInForce", timeInForce)
        builder.put_url("quantity", quantity)
        builder.put_url("quoteOrderQty", quoteOrderQty)
        builder.put_url("price", price)
        builder.put_url("newClientOrderId", newClientOrderId)
        builder.put_url("stopPrice", stopPrice)
        builder.put_url("icebergQty", icebergQty)
        builder.put_url("newOrderRespType", newOrderRespType)

        request = self.__create_request_by_post_with_signature("/api/v3/order", builder)

        def parse(json_wrapper):
            information = NewOrder.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
       
    def cancel_order(self, symbol, orderId, origClientOrderId, newClientOrderId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("origClientOrderId", origClientOrderId)
        builder.put_url("newClientOrderId", newClientOrderId)

        request = self.__create_request_by_delete_with_signature("/api/v3/order", builder)

        def parse(json_wrapper):
            information = CancelOrder.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
      
    def get_order(self, symbol, orderId, origClientOrderId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("origClientOrderId", origClientOrderId)

        request = self.__create_request_by_get_with_signature("/api/v3/order", builder)

        def parse(json_wrapper):
            information = Order.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
      
    def get_open_orders(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_signature("/api/v3/openOrders", builder)

        def parse(json_wrapper):
            order_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                order = Order.json_parse(item)
                order_list.append(order)
            return order_list

        request.json_parser = parse
        return request
      
    def get_all_orders(self, symbol, orderId, startTime, endTime, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/api/v3/allOrders", builder)

        def parse(json_wrapper):
            order_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                order = Order.json_parse(item)
                order_list.append(order)
            return order_list

        request.json_parser = parse
        return request
      
    def post_oco(self, symbol, listClientOrderId, side, quantity,
                limitClientOrderId, price, limitIcebergQty, stopClientOrderId, stopPrice, stopLimitPrice,
                stopIcebergQty, stopLimitTimeInForce, newOrderRespType):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(side, "side")
        check_should_not_none(quantity, "quantity")
        check_should_not_none(price, "price")
        check_should_not_none(stopPrice, "stopPrice")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("listClientOrderId", listClientOrderId)
        builder.put_url("side", side)
        builder.put_url("quantity", quantity)
        builder.put_url("limitClientOrderId", limitClientOrderId)
        builder.put_url("price", price)
        builder.put_url("limitIcebergQty", limitIcebergQty)
        builder.put_url("stopClientOrderId", stopClientOrderId)
        builder.put_url("stopPrice", stopPrice)
        builder.put_url("stopLimitPrice", stopLimitPrice)
        builder.put_url("stopIcebergQty", stopIcebergQty)
        builder.put_url("stopLimitTimeInForce", stopLimitTimeInForce)
        builder.put_url("newOrderRespType", newOrderRespType)

        request = self.__create_request_by_post_with_signature("/api/v3/order/oco", builder)

        def parse(json_wrapper):
            information = NewOco.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
 
    def get_open_oco(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/api/v3/openOrderList", builder)

        def parse(json_wrapper):
            oco_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                oco = Oco.json_parse(item)
                oco_list.append(oco)
            return oco_list

        request.json_parser = parse
        return request
 
    def get_all_oco(self, fromId, startTime, endTime, limit):
        builder = UrlParamsBuilder()
        builder.put_url("fromId", fromId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/api/v3/allOrderList", builder)

        def parse(json_wrapper):
            oco_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                oco = Oco.json_parse(item)
                oco_list.append(oco)
            return oco_list

        request.json_parser = parse
        return request
 
    def get_oco(self, orderListId, origClientOrderId):
        builder = UrlParamsBuilder()
        builder.put_url("orderListId", orderListId)
        builder.put_url("origClientOrderId", origClientOrderId)

        request = self.__create_request_by_get_with_signature("/api/v3/orderList", builder)

        def parse(json_wrapper):
            oco = Oco.json_parse(json_wrapper)
            return oco

        request.json_parser = parse
        return request
           
    def cancel_oco(self, symbol, orderListId, listClientOrderId, newClientOrderId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderListId", orderListId)
        builder.put_url("listClientOrderId", listClientOrderId)
        builder.put_url("newClientOrderId", newClientOrderId)

        request = self.__create_request_by_delete_with_signature("/api/v3/orderList", builder)

        def parse(json_wrapper):
            information = CancelOco.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
              
    def get_account_information(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/api/v3/account", builder)

        def parse(json_wrapper):
            information = AccountInformation.json_parse(json_wrapper)
            return information

        request.json_parser = parse
        return request
          
    def get_account_trades(self, symbol, startTime, endTime, fromId, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("fromId", fromId)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/api/v3/myTrades", builder)

        def parse(json_wrapper):
            trade_list = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                trade = MyTrade.json_parse(item)
                trade_list.append(trade)
            return trade_list

        request.json_parser = parse
        return request
          
    def post_margin_transfer(self, asset, amount, transferType):
        check_should_not_none(asset, "asset")
        check_should_not_none(amount, "amount")
        check_should_not_none(transferType, "transferType")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("amount", amount)
        builder.put_url("type", transferType)

        request = self.__create_request_by_post_with_signature("/sapi/v1/margin/transfer", builder)

        def parse(json_wrapper):
            tranId = json_wrapper.get_int("tranId")
            return tranId

        request.json_parser = parse
        return request
          
    def post_margin_borrow(self, asset, amount):
        check_should_not_none(asset, "asset")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("amount", amount)

        request = self.__create_request_by_post_with_signature("/sapi/v1/margin/loan", builder)

        def parse(json_wrapper):
            tranId = json_wrapper.get_int("tranId")
            return tranId

        request.json_parser = parse
        return request
          
    def post_margin_repay(self, asset, amount):
        check_should_not_none(asset, "asset")
        check_should_not_none(amount, "amount")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("amount", amount)

        request = self.__create_request_by_post_with_signature("/sapi/v1/margin/repay", builder)

        def parse(json_wrapper):
            tranId = json_wrapper.get_int("tranId")
            return tranId

        request.json_parser = parse
        return request
          
    def get_margin_asset(self, asset):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)

        request = self.__create_request_by_get_with_apikey("/sapi/v1/margin/asset", builder)

        def parse(json_wrapper):
            asset = MarginAsset.json_parse(json_wrapper)
            return asset

        request.json_parser = parse
        return request
          
    def get_margin_pair(self, symbol):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_apikey("/sapi/v1/margin/pair", builder)

        def parse(json_wrapper):
            result = MarginPair.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request
         
    def get_margin_assets(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_apikey("/sapi/v1/margin/allAssets", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                element = MarginAsset.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
           
    def get_margin_pairs(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_apikey("/sapi/v1/margin/allPairs", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                element = MarginPair.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_priceindex(self, symbol):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_apikey("/sapi/v1/margin/priceIndex", builder)

        def parse(json_wrapper):
            result = MarginPriceIndex.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request
       
    def post_margin_order(self, symbol, side, ordertype, 
                quantity, price, stopPrice, newClientOrderId, icebergQty, newOrderRespType, sideEffectType, timeInForce):
        check_should_not_none(symbol, "symbol")
        check_should_not_none(side, "side")
        check_should_not_none(ordertype, "ordertype")
        check_should_not_none(quantity, "quantity")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("side", side)
        builder.put_url("type", ordertype)
        builder.put_url("quantity", quantity)
        builder.put_url("price", price)
        builder.put_url("stopPrice", stopPrice)
        builder.put_url("newClientOrderId", newClientOrderId)
        builder.put_url("icebergQty", icebergQty)
        builder.put_url("newOrderRespType", newOrderRespType)
        builder.put_url("sideEffectType", sideEffectType)
        builder.put_url("timeInForce", timeInForce)

        request = self.__create_request_by_post_with_signature("/sapi/v1/margin/order", builder)

        def parse(json_wrapper):
            result = MarginNewOrder.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request

    def cancel_margin_order(self, symbol, orderId, origClientOrderId, newClientOrderId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("origClientOrderId", origClientOrderId)
        builder.put_url("newClientOrderId", newClientOrderId)

        request = self.__create_request_by_delete_with_signature("/sapi/v1/margin/order", builder)

        def parse(json_wrapper):
            result = MarginCancelOrder.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request
        
    def get_margin_transfer(self, asset, transferType, startTime, endTime, current, size):
        check_should_not_none(transferType, "transferType")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("type", transferType)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("current", current)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/transfer", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.get_array("rows")
            for item in data_list.get_items():
                element = MarginTransfer.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_loan(self, asset, txId, startTime, endTime, current, size):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("txId", txId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("current", current)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/loan", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.get_array("rows")
            for item in data_list.get_items():
                element = MarginLoan.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_repay(self, asset, txId, startTime, endTime, current, size):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("txId", txId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("current", current)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/repay", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.get_array("rows")
            for item in data_list.get_items():
                element = MarginRepay.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_interest(self, asset, startTime, endTime, current, size):
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("current", current)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/interestHistory", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.get_array("rows")
            for item in data_list.get_items():
                element = MarginInterest.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_force_liquidation(self, startTime, endTime, current, size):
        builder = UrlParamsBuilder()
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("current", current)
        builder.put_url("size", size)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/forceLiquidationRec", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.get_array("rows")
            for item in data_list.get_items():
                element = MarginForceLiquidation.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_account(self):
        builder = UrlParamsBuilder()

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/account", builder)

        def parse(json_wrapper):
            result = MarginAccount.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_order(self, symbol, orderId, origClientOrderId):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("origClientOrderId", origClientOrderId)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/order", builder)

        def parse(json_wrapper):
            result = MarginOrder.json_parse(json_wrapper)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_open_orders(self, symbol):
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/openOrders", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                element = MarginOrder.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_orders(self, symbol, orderId, startTime, endTime, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("orderId", orderId)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/allOrders", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                element = MarginOrder.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_trades(self, symbol, startTime, endTime, fromId, limit):
        check_should_not_none(symbol, "symbol")
        builder = UrlParamsBuilder()
        builder.put_url("symbol", symbol)
        builder.put_url("startTime", startTime)
        builder.put_url("endTime", endTime)
        builder.put_url("fromId", fromId)
        builder.put_url("limit", limit)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/myTrades", builder)

        def parse(json_wrapper):
            result = list()
            data_list = json_wrapper.convert_2_array()
            for item in data_list.get_items():
                element = MarginTrade.json_parse(item)
                result.append(element)
            return result

        request.json_parser = parse
        return request
      
    def get_margin_max_borrow(self, asset):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/maxBorrowable", builder)

        def parse(json_wrapper):
            result = json_wrapper.get_float("amount")
            return result

        request.json_parser = parse
        return request
      
    def get_margin_max_transfer(self, asset):
        check_should_not_none(asset, "asset")
        builder = UrlParamsBuilder()
        builder.put_url("asset", asset)

        request = self.__create_request_by_get_with_signature("/sapi/v1/margin/maxTransferable", builder)

        def parse(json_wrapper):
            result = json_wrapper.get_float("amount")
            return result

        request.json_parser = parse
        return request
      
    def start_user_data_stream(self, accountType):
        builder = UrlParamsBuilder()

        if(accountType == AccountType.SPOT):
            request = self.__create_request_by_post_with_apikey("/api/v3/userDataStream", builder)
        elif(accountType == AccountType.MARGIN):
            request = self.__create_request_by_post_with_apikey("/sapi/v1/userDataStream", builder)

        def parse(json_wrapper):
            result = json_wrapper.get_string("listenKey")
            return result

        request.json_parser = parse
        return request
      
    def keep_user_data_stream(self, listenKey, accountType):
        check_should_not_none(listenKey, "listenKey")
        builder = UrlParamsBuilder()
        builder.put_url("listenKey", listenKey)

        if(accountType == AccountType.SPOT):
            request = self.__create_request_by_put_with_apikey("/api/v3/userDataStream", builder)
        elif(accountType == AccountType.MARGIN):
            request = self.__create_request_by_put_with_apikey("/sapi/v3/userDataStream", builder)

        def parse(json_wrapper):
            result = "OK"
            return result

        request.json_parser = parse
        return request
      
        