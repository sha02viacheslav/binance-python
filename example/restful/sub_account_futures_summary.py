from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_futures_summary = request_client.sub_account_futures_summary()

print("======= Get Summary of Sub-account's Margin Account (For Master Account) =======")
print("totalInitialMargin: ", sub_account_futures_summary.totalInitialMargin)
print("totalMaintMargin: ", sub_account_futures_summary.totalMaintMargin)
print("totalMarginBalance: ", sub_account_futures_summary.totalMarginBalance)
print("totalOpenOrderInitialMargin: ", sub_account_futures_summary.totalOpenOrderInitialMargin)
print("totalPositionInitialMargin: ", sub_account_futures_summary.totalPositionInitialMargin)
print("totalUnrealizedProfit: ", sub_account_futures_summary.totalUnrealizedProfit)
print("totalWalletBalance: ", sub_account_futures_summary.totalWalletBalance)
print("asset: ", sub_account_futures_summary.asset)
print("")
print("=== subAccountList ===")
for sub_account in sub_account_futures_summary.subAccount:
	print("email: ", sub_account.email)
	print("totalInitialMargin: ", sub_account.totalInitialMargin)
	print("totalMaintMargin: ", sub_account.totalMaintMargin)
	print("totalMarginBalance: ", sub_account.totalMarginBalance)
	print("totalOpenOrderInitialMargin: ", sub_account.totalOpenOrderInitialMargin)
	print("totalPositionInitialMargin: ", sub_account.totalPositionInitialMargin)
	print("totalUnrealizedProfit: ", sub_account.totalUnrealizedProfit)
	print("totalWalletBalance: ", sub_account.totalWalletBalance)
	print("asset: ", sub_account.asset)
	print("")
print("======================")
print("===============================================================================")
