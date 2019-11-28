import requests
from binance.exception.binanceapiexception import BinanceApiException
from binance.impl.utils.etfresult import etf_result_check
from binance.impl.utils import *


def check_response(json_wrapper):
    if json_wrapper.contain_key("success"):
        success = json_wrapper.get_boolean("success")
        if success is False:
            err_code = etf_result_check(json_wrapper.get_int("code"))
            err_msg = json_wrapper.get_string("message")
            if err_code == "":
                raise BinanceApiException(BinanceApiException.EXEC_ERROR, "[Executing] " + err_msg)
            else:
                raise BinanceApiException(BinanceApiException.EXEC_ERROR, "[Executing] " + err_code + ": " + err_msg)
    elif json_wrapper.contain_key("code"):
        code = json_wrapper.get_int("code")
        msg = json_wrapper.get_string_or_default("msg", "")
        if code != 200:
            raise BinanceApiException(BinanceApiException.EXEC_ERROR, "[Executing] " + str(code) + ": " + msg)


def call_sync(request):
    if request.method == "GET":
        response = requests.get(request.host + request.url, headers=request.header)
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)
    elif request.method == "POST":
        response = requests.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        json_wrapper = parse_json_from_string(response.text)
        check_response(json_wrapper)
        return request.json_parser(json_wrapper)
