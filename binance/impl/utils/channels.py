import json
from binance.impl.utils.timeservice import get_current_timestamp
from binance.model import DepthStep


def kline_channel(symbol, interval):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@kline_" + interval)
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def aggregate_trade_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@aggTrade")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def trade_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@trade")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_miniticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@miniTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_miniticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!miniTicker@arr")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_ticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@ticker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_ticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!ticker@arr")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def symbol_bookticker_channel(symbol):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@bookTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def all_bookticker_channel():
    channel = dict()
    channel["params"] = list()
    channel["params"].append("!bookTicker")
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)

def book_depth_channel(symbol, limit):
    channel = dict()
    channel["params"] = list()
    channel["params"].append(symbol + "@depth" + str(limit))
    channel["id"] = get_current_timestamp()
    channel["method"] = "SUBSCRIBE"
    return json.dumps(channel)