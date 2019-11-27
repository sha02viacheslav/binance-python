from binance import RequestClient
from binance.constant.test import *
from binance.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
all_coins_information = request_client.all_coins_information()

print("======= All Coins' Information (USER_DATA) =======")
if all_coins_information and len(all_coins_information):
    for coin_information in all_coins_information:
        print("coin:", coin_information.coin)
        print("depositAllEnable:", coin_information.depositAllEnable)
        print("free:", coin_information.free)
        print("freeze:", coin_information.freeze)
        print("ipoable:", coin_information.ipoable)
        print("ipoing:", coin_information.ipoing)
        print("isLegalMoney:", coin_information.isLegalMoney)
        print("locked:", coin_information.locked)
        print("name:", coin_information.name)
        print("storage:", coin_information.storage)
        print("trading:", coin_information.trading)
        print("withdrawAllEnable:", coin_information.withdrawAllEnable)
        print("withdrawing:", coin_information.withdrawing)
        if coin_information.network_list and len(coin_information.network_list):
            j = 0
            for network in coin_information.network_list:
                j = j + 1
                print("\t=== Network ", j, "===")
                print("\t addressRegex:", network.addressRegex)
                print("\t coin:", network.coin)
                print("\t depositEnable:", network.depositEnable)
                print("\t isDefault:", network.isDefault)
                print("\t memoRegex:", network.memoRegex)
                print("\t name:", network.name)
                print("\t network:", network.network)
                print("\t resetAddressStatus:", network.resetAddressStatus)
                print("\t specialTips:", network.specialTips)
                print("\t withdrawDesc:", network.withdrawDesc)
                print("\t withdrawEnable:", network.withdrawEnable)
                print("\t withdrawFee:", network.withdrawFee)
                print("\t withdrawIntegerMultiple:", network.withdrawIntegerMultiple)
                print("\t withdrawMin:", network.withdrawMin)
                print()
            print()
        else:
            print("=== No Network ===")
print("==================================================")
