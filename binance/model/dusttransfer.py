class TransferLog:

    def __init__(self):
        self.amount = 0.0
        self.fromAsset = ""
        self.operateTime = 0
        self.serviceChargeAmount = 0.0
        self.tranId = None
        self.transferedAmount = 0.0


class DustTransfer:

    def __init__(self):
        self.totalServiceCharge = 0.0
        self.totalTransfered = 0.0
        self.transferResult = list()

    @staticmethod
    def json_parse(json_data):
        dust_transfer = DustTransfer()
        dust_transfer.totalServiceCharge = json_data.get_float("totalServiceCharge")
        dust_transfer.totalTransfered = json_data.get_float("totalTransfered")
        list_array = json_data.get_array("transferResult")
        transfer_logs = list()
        
        for item in list_array.get_items():
            transfer_log = TransferLog()
            transfer_log.amount = item.get_float("amount")
            transfer_log.fromAsset = item.get_string("fromAsset")
            transfer_log.operateTime = item.get_int("operateTime")
            transfer_log.serviceChargeAmount = item.get_float("serviceChargeAmount")
            transfer_log.tranId = item.get_int("tranId")
            transfer_log.transferedAmount = item.get_float("transferedAmount")
            transfer_logs.append(transfer_log)

        dust_transfer.transferResult = transfer_logs
        return dust_transfer