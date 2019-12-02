from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

deposit_histories = request_client.sub_account_deposit_history(email = "123@test.com", coin = "BTC", status = None, 
                                    startTime = None, endTime = None, offest = None)

print("======= Get Sub-account Deposit History (For Master Account) =======")
PrintMix.print_data(deposit_histories)
print("====================================================================")





