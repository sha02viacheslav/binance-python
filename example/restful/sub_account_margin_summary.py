from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_margin_summary = request_client.sub_account_margin_summary()

print("======= Get Summary of Sub-account's Margin Account (For Master Account) =======")
print("totalAssetOfBtc: ", sub_account_margin_summary.totalAssetOfBtc)
print("totalLiabilityOfBtc: ", sub_account_margin_summary.totalLiabilityOfBtc)
print("totalNetAssetOfBtc: ", sub_account_margin_summary.totalNetAssetOfBtc)
print("")
print("=== subAccountList ===")
for sub_account in sub_account_margin_summary.subAccountList:
	print("email: ", sub_account.email)
	print("totalAssetOfBtc: ", sub_account.totalAssetOfBtc)
	print("totalLiabilityOfBtc: ", sub_account.totalLiabilityOfBtc)
	print("totalNetAssetOfBtc: ", sub_account.totalNetAssetOfBtc)
	print("")
print("======================")
print("===============================================================================")
