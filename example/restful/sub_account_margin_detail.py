from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

sub_account_margin_detail = request_client.sub_account_margin_detail(email = "123@test.com")

print("======= Get Detail on Sub-account's Margin Account (For Master Account) =======")
print("email: ", sub_account_margin_detail.email)
print("marginLevel: ", sub_account_margin_detail.marginLevel)
print("totalAssetOfBtc: ", sub_account_margin_detail.totalAssetOfBtc)
print("totalLiabilityOfBtc: ", sub_account_margin_detail.totalLiabilityOfBtc)
print("totalNetAssetOfBtc: ", sub_account_margin_detail.totalNetAssetOfBtc)
print("=== marginTradeCoeffVo ===")
print("\tLiquidation margin ratio: ", sub_account_margin_detail.marginTradeCoeffVo.forceLiquidationBar)
print("\tMargin call margin ratio: ", sub_account_margin_detail.marginTradeCoeffVo.marginCallBar)
print("\tInitial margin ratio: ", sub_account_margin_detail.marginTradeCoeffVo.normalBar)
print("==========================")
print("")
print("=== marginUserAssetVoList ===")
for marginUserAssetVo in sub_account_margin_detail.marginUserAssetVoList:
	print("asset: ", marginUserAssetVo.asset)
	print("borrowed: ", marginUserAssetVo.borrowed)
	print("free: ", marginUserAssetVo.free)
	print("interest: ", marginUserAssetVo.interest)
	print("locked: ", marginUserAssetVo.locked)
	print("netAsset: ", marginUserAssetVo.netAsset)
	print("")
print("============================")
print("===============================================================================")
