from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_futures_detail = request_client.get_sub_account_futures_detail(email = "123@test.com")

print("======= Get Detail on Sub-account's Futures Account (For Master Account) =======")
print("email: ", sub_account_futures_detail.email)
print("canDeposit: ", sub_account_futures_detail.canDeposit)
print("canTrade: ", sub_account_futures_detail.canTrade)
print("canWithdraw: ", sub_account_futures_detail.canWithdraw)
print("feeTier: ", sub_account_futures_detail.feeTier)
print("maxWithdrawAmount: ", sub_account_futures_detail.maxWithdrawAmount)
print("totalInitialMargin: ", sub_account_futures_detail.totalInitialMargin)
print("totalMaintMargin: ", sub_account_futures_detail.totalMaintMargin)
print("totalMarginBalance: ", sub_account_futures_detail.totalMarginBalance)
print("totalOpenOrderInitialMargin: ", sub_account_futures_detail.totalOpenOrderInitialMargin)
print("totalPositionInitialMargin: ", sub_account_futures_detail.totalPositionInitialMargin)
print("totalUnrealizedProfit: ", sub_account_futures_detail.totalUnrealizedProfit)
print("totalWalletBalance: ", sub_account_futures_detail.totalWalletBalance)
print("asset: ", sub_account_futures_detail.asset)
print("updateTime: ", sub_account_futures_detail.updateTime)
print("")
print("=== Assets ===")
for asset in sub_account_futures_detail.assets:
	print("asset: ", asset.asset)
	print("initialMargin: ", asset.initialMargin)
	print("maintMargin: ", asset.maintMargin)
	print("marginBalance: ", asset.marginBalance)
	print("maxWithdrawAmount: ", asset.maxWithdrawAmount)
	print("openOrderInitialMargin: ", asset.openOrderInitialMargin)
	print("positionInitialMargin: ", asset.positionInitialMargin)
	print("unrealizedProfit: ", asset.unrealizedProfit)
	print("walletBalance: ", asset.walletBalance)
	print("")
print("===============")
print("=================================================================================")
