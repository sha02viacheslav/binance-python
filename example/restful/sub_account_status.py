from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_accouont_status = request_client.sub_account_status(email = "123@test.com")

print("======= Get Sub-account's Status on Margin/Futures(For Master Account) =======")
PrintMix.print_data(sub_accouont_status)
print("==============================================================================")





