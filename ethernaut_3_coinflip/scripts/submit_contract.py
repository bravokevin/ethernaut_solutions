from brownie import Contract
from scripts.hack import INSTANCE_ADDRESS, ACCOUNT

ETHERNAUT_ABI =[
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "player",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "contract Level",
                "name": "level",
                "type": "address"
            }
        ],
        "name": "LevelCompletedLog",
        "type": "event",
        "signature": "0x9dfdf7e3e630f506a3dfe38cdbe34e196353364235df33e5a3b588488d9a1e78"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "player",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "instance",
                "type": "address"
            }
        ],
        "name": "LevelInstanceCreatedLog",
        "type": "event",
        "signature": "0x7bf7f1ed7f75e83b76de0ff139966989aff81cb85aac26469c18978d86aac1c2"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event",
        "signature": "0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0"
    },
    {
        "inputs": [
            {
                "internalType": "contract Level",
                "name": "_level",
                "type": "address"
            }
        ],
        "name": "createLevelInstance",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function",
        "payable": True,
        "signature": "0xdfc86b17"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True,
        "signature": "0x8da5cb5b"
    },
    {
        "inputs": [
            {
                "internalType": "contract Level",
                "name": "_level",
                "type": "address"
            }
        ],
        "name": "registerLevel",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
        "signature": "0x202023d4"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
        "signature": "0x715018a6"
    },
    {
        "inputs": [
            {
                "internalType": "address payable",
                "name": "_instance",
                "type": "address"
            }
        ],
        "name": "submitLevelInstance",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
        "signature": "0xc882d7c2"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
        "signature": "0xf2fde38b"
    }
]

ETHERNAUT_CONTRACT_ADDRESS = "0xD991431D8b033ddCb84dAD257f4821E9d5b38C33"

def submit_the_contract():
    ethernaut_contract = Contract.from_abi("Ethernaut",ETHERNAUT_CONTRACT_ADDRESS, ETHERNAUT_ABI)
    print("Submiting instance")

    tx = ethernaut_contract.submitLevelInstance(
        INSTANCE_ADDRESS, 
        {"from": ACCOUNT}
    )


    if("LevelCompletedLog"  in tx.events):
        print("Instance submitted. Level passed. WOHOOO!")
        print("refresh the page of ethernaut")
    else:
        print("Instance submitted. But you don't break the level :(")



def main():
    submit_the_contract()