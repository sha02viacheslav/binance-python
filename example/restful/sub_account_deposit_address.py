from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_deposit_address = request_client.sub_account_deposit_address(email = "123@test.com", 
															coin = "BTC", network = None)

print("======= Get Sub-account Deposit Address (For Master Account) =======")
PrintMix.print_data(sub_account_deposit_address)
print("====================================================================")
