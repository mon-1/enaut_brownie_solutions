from brownie import accounts, network, config, GatekeeperTwo, gateKeeperTwoATK

def main():
    instanceAddress = "0x1383308E27B9Cdb920aCdb0afc3Bd73DdF37C69D"

    player = accounts.add(config["wallets"]["from_key"]) 
    gateKeeper = GatekeeperTwo.at(instanceAddress)
    print(f"Entrant? :{gateKeeper.entrant()}")#default 0 address returned
    gateKeeperATK = gateKeeperTwoATK.deploy(instanceAddress, {"from": player})
    print(f"Entrant? :{gateKeeper.entrant()}") #RETURNS player address if successful
    
