from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc
from binance.base.printobject import *

class RateLimit:

    def __init__(self):
        self.rateLimitType = ""
        self.interval = ""
        self.intervalNum = 0
        self.limit = 0


class ExchangeFilter:

    def __init__(self):
        self.filterType = ""
        self.maxOrders = 0


class Symbol:

    def __init__(self):
        self.symbol = ""
        self.status = ""
        self.baseAsset = ""
        self.baseAssetPrecision = 0
        self.quoteAsset = ""
        self.quotePrecision = 0
        self.orderTypes = list()
        self.icebergAllowed = False
        self.ocoAllowed = False
        self.isSpotTradingAllowed = False
        self.isMarginTradingAllowed = False
        self.filters = list()


class ExchangeInformation:

    def __init__(self):
        self.timezone = ""
        self.serverTime = 0
        self.rateLimits = list()
        self.exchangeFilters = list()
        self.symbols = list()

    @staticmethod
    def json_parse(json_data):
        exchange_information = ExchangeInformation()
        exchange_information.timezone = json_data.get_string("timezone")
        exchange_information.serverTime = convert_cst_in_millisecond_to_utc(json_data.get_int("serverTime"))

        PrintMix.print_data(json_data.get_array("exchangeFilters"))

        list_array = json_data.get_array("rateLimits")
        rate_limit_list = list()
        for item in list_array.get_items():
            rate_limit = RateLimit()
            rate_limit.rateLimitType = item.get_string("rateLimitType")
            rate_limit.interval = item.get_string("interval")
            rate_limit.intervalNum = item.get_int("intervalNum")
            rate_limit.limit = item.get_int("limit")

            rate_limit_list.append(rate_limit)
        exchange_information.rateLimits = rate_limit_list

        list_array = json_data.get_array("exchangeFilters")
        exchange_filter_list = list()
        for item in list_array.get_items():
            exchange_filter = ExchangeFilter()
            exchange_filter.filterType = item.get_string("filterType")
            if exchange_filter.filterType == "EXCHANGE_MAX_NUM_ORDERS":
                exchange_filter.maxNumOrders = item.get_int("maxNumOrders")
            elif  exchange_filter.filterType == "EXCHANGE_MAX_ALGO_ORDERS":
                exchange_filter.maxNumAlgoOrders = item.get_int("maxNumAlgoOrders")

            exchange_filter_list.append(exchange_filter)
        exchange_information.exchangeFilters = exchange_filter_list

        list_array = json_data.get_array("symbols")
        symbol_list = list()
        for item in list_array.get_items():
            symbol = Symbol()
            symbol.symbol = item.get_string("symbol")
            symbol.status = item.get_string("status")
            symbol.baseAsset = item.get_string("baseAsset")
            symbol.baseAssetPrecision = item.get_int("baseAssetPrecision")
            symbol.quoteAsset = item.get_string("quoteAsset")
            symbol.quotePrecision = item.get_int("quotePrecision")
            symbol.orderTypes = item.get_object("orderTypes").convert_2_list()
            symbol.icebergAllowed = item.get_boolean("icebergAllowed")
            symbol.ocoAllowed = item.get_boolean("ocoAllowed")
            symbol.isSpotTradingAllowed = item.get_boolean("isSpotTradingAllowed")
            symbol.isMarginTradingAllowed = item.get_boolean("isMarginTradingAllowed")

            val_list = item.get_array("filters")
            filter_list = list()
            for element in val_list.get_items():
                filter_list.append(element.convert_2_dict())
            symbol.filters = filter_list

            symbol_list.append(symbol)
        exchange_information.symbols = symbol_list

        return exchange_information

