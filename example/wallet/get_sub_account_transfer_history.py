from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_transfer_history = request_client.get_sub_account_transfer_history(email = "123@test.com", 
					startTime = None, endTime = None, page = None, limit = None)

print("======= Query Sub-account Transfer History(For Master Account) =======")
PrintMix.print_data(sub_account_transfer_history)
print("======================================================================")