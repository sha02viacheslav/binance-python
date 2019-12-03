from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc
from binance.base.printobject import *

class Record:

    def __init__(self):
        self.amount = 0.0
        self.asset = ""
        self.divTime = 0
        self.enInfo = ""
        self.tranId = None

 
class AssetDividendRecord:

    def __init__(self):
        self.total = 0
        self.rows = list()

    @staticmethod
    def json_parse(json_data):
        asset_dividend_record = AssetDividendRecord()
        asset_dividend_record.total = json_data.get_int("total")
        list_array = json_data.get_array("rows")
        rows = list()
        
        for item in list_array.get_items():
            record = Record()
            record.amount = item.get_float("amount")
            record.asset = item.get_string("asset")
            record.divTime = convert_cst_in_millisecond_to_utc(item.get_int("divTime"))
            record.enInfo = item.get_string("enInfo")
            record.tranId = item.get_int("tranId")

            rows.append(record)

        asset_dividend_record.rows = rows
        return asset_dividend_record