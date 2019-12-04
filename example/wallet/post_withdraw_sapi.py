from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)


withdraw_id_new = request_client.post_withdraw_sapi(coin = "BTC", address = "xxxxx", amount = 0.001, network = None,
                                            addressTag = None, name = None)

print("======= Withdraw [SAPI] =======")
print(withdraw_id_new)
print("===============================")


# withdraw_id_ret = request_client.post_cancel_withdraw(withdraw_id=withdraw_id_formated)
# print("Cancel Withdraw ", withdraw_id_ret)





