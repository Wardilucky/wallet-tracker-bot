from web3 import Web3
from config import INFURA_API_KEY, WATCHED_WALLETS

web3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/9a098e5d6cc746c8b6ceaec3f1238e41"))
last_checked_block = web3.eth.block_number

def check_evm_transactions():
    global last_checked_block
    new_txs = []
    latest_block = web3.eth.block_number

    for block_num in range(last_checked_block + 1, latest_block + 1):
        block = web3.eth.get_block(block_num, full_transactions=True)
        for tx in block.transactions:
            if tx["to"] and tx["to"].lower() in [addr.lower() for addr in WATCHED_WALLETS["evm"]]:
                new_txs.append(tx)

    last_checked_block = latest_block
    return new_txs
