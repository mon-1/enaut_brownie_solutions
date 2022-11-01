from brownie import config, Token, accounts, network
def main():
    player = accounts.add(config["wallets"]["from_key"]) 

    InstanceAddress = "0x9a98de8DB0FddcC2A9A63509b57161EA6bf9528d"

    token = Token.at(InstanceAddress)
    token.transfer(InstanceAddress, 21, {"from": player})
    print(f"Balance is : {token.balanceOf(player)}")