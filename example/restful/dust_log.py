from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

dust_logs = request_client.dust_log()

print("======= DustLog (USER_DATA) =======")
print("Total counts of exchange: ", dust_logs.total)
print("")
idx = 0
for item in dust_logs.rows:
	idx = idx + 1
	print("Dust Log ", str(idx), ":\n")
	print("Total transfered BNB amount for this exchange: ", item.transfered_total)
	print("Total service charge amount for this exchange: ", item.service_charge_total)
	print("tran_id: ", item.tran_id)
	print("operate_time: ", item.operate_time)
	jdx = 0
	for jtem in item.logs:
		jdx = jdx + 1
		print("\tLog", str(jdx), ":\n")
		print("\ttranId: ", jtem.tranId)
		print("\tserviceChargeAmount: ", jtem.serviceChargeAmount)
		print("\tuid: ", jtem.uid)
		print("\tamount: ", jtem.amount)
		print("\toperateTime: ", jtem.operateTime)
		print("\ttransferedAmount: ", jtem.transferedAmount)
		print("\tfromAsset: ", jtem.fromAsset)
		print("")
	print("")
print("=====================================")



