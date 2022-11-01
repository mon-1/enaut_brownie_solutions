from brownie import config, network, accounts, King, KingATK

InstanceAddress = "0xF3A48a29C1213E9f566b687b3F5Cf305a5b3926f"

player = accounts.add(config["wallets"]["from_key"]) 
def main():

    king = King.at(InstanceAddress)

    kingATK = KingATK.deploy({"from": player})
    kingATK.atk(InstanceAddress, {"from": player, "value":1000000000000001 })
