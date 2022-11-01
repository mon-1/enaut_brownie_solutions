from brownie import config, accounts, MagicNum, magicNumATK
InstanceAddress = "0x56513a61c44366978F07262D1B57A442a7434a52"
player = accounts.add(config["wallets"]["from_key"]) 
magicNum = MagicNum.at(InstanceAddress)
def main():
    magicNum_solve = magicNumATK.deploy(InstanceAddress, {"from":player})
    magicNum_solve.attack()
    print(f"codeSize: {magicNum_solve.getCodeSize()}")