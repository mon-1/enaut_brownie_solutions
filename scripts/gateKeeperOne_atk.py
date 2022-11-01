from brownie import accounts, network, config, GatekeeperOne, GateKeeperATK

def main():
    instanceAddress = "0x7345842756810661EDe09dE0b8660136EB3473FD"

    player = accounts.add(config["wallets"]["from_key"]) 
    gateKeeper = GatekeeperOne.at(instanceAddress)
    gateKeeperATK = GateKeeperATK.deploy(instanceAddress, {"from": player})
    print(f"Entrant? :{gateKeeper.entrant()}") #default 0 address returned
    gateKeeperATK.atk({"from": player})
    print(f"Entrant? :{gateKeeper.entrant()}") #RETURNS player address if successful
    
