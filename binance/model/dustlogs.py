from binance.impl.utils.timeservice import convert_cst_in_millisecond_to_utc
from binance.base.printobject import *

class Log:

    def __init__(self):
        self.tranId = None
        self.serviceChargeAmount = 0.0
        self.uid = None
        self.amount = 0.0
        self.operateTime = ""
        self.transferedAmount = 0.0
        self.fromAsset = ""

class DustLog:

    def __init__(self):
        self.transfered_total = 0.0
        self.service_charge_total = 0.0
        self.tran_id = None
        self.operate_time = ""
        self.logs = list()

class DustLogs:

    def __init__(self):
        self.total = 0
        self.rows = list()

    @staticmethod
    def json_parse(json_data):
        dust_logs = DustLogs()
        dust_logs.total = json_data.get_int("total")
        list_array = json_data.get_array("rows")
        rows = list()
        
        for item in list_array.get_items():
            dust_log = DustLog()
            dust_log.transfered_total = item.get_float("transfered_total")
            dust_log.service_charge_total = item.get_float("service_charge_total")
            dust_log.tran_id = item.get_int("tran_id")
            dust_log.operate_time = item.get_string("operate_time")
            dust_log.logs = list()

            val_list = item.get_array("logs")
            for element in val_list.get_items():
                log = Log()
                log.tranId = element.get_int("tranId")
                log.serviceChargeAmount = element.get_float("serviceChargeAmount")
                log.uid = element.get_int("uid")
                log.amount = element.get_float("amount")
                log.operateTime = element.get_string("operateTime")
                log.transferedAmount = element.get_float("transferedAmount")
                log.fromAsset = element.get_string("fromAsset")
                dust_log.logs.append(log)

            rows.append(dust_log)

        dust_logs.rows = rows
        return dust_logs