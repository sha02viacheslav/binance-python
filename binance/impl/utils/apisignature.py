import base64
import hashlib
import hmac
import datetime
from urllib import parse
import urllib.parse
from binance.exception.binanceapiexception import BinanceApiException


def create_signature(secret_key, builder):
    if secret_key is None or secret_key == "":
        raise BinanceApiException(BinanceApiException.KEY_MISSING,  "Secret key are required")

    # 对参数进行排序:
    keys = sorted(builder.param_map.keys())
    # 加入&
    query_string = '&'.join(['%s=%s' % (key, parse.quote(builder.param_map[key], safe='')) for key in keys])

    signature = hmac.new(secret_key.encode(), msg=query_string.encode(), digestmod=hashlib.sha256).hexdigest()
    
    builder.put_url("signature", signature)


def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
