from brownie import accounts, config, Testing
from web3 import Web3
import os

ACCOUNT = accounts.add(config["wallets"]["from_key"])

w3 = Web3(Web3.HTTPProvider(os.getenv("PROJECT_ENDPOINT")))

def deploy():

    contract_instance = Testing.deploy(
        {"from": ACCOUNT},
        publish_source=True
    )

def main():
    deploy()