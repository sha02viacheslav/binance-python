from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_futures_positionrisk = request_client.sub_account_futures_positionrisk(email = "123@test.com")

print("======= Get Futures Postion-Risk of Sub-account (For Master Account) =======")
PrintMix.print_data(sub_account_futures_positionrisk)
print("============================================================================")





