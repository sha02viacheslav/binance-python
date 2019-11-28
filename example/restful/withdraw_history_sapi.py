from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

withdraw_histories = request_client.withdraw_history_sapi(coin = None, status = None, offset = None, limit = None, 
                                                            startTime = None, endTime = None)

print("======= Withdraw History（supporting network） (USER_DATA) =======")
PrintMix.print_data(withdraw_histories)
print("=================================================================")





