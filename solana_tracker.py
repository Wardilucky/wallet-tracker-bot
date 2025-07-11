from solana.rpc.api import Client
from solders.pubkey import Pubkey
from config import SOLANA_RPC_URL, WATCHED_WALLETS

solana_client = Client(SOLANA_RPC_URL)
seen_signatures = set()

def check_solana_transactions():
    txs = []
    for addr in WATCHED_WALLETS["solana"]:
        pubkey = Pubkey.from_string(addr)
        resp = solana_client.get_signatures_for_address(pubkey, limit=5)
        for tx in resp.value:
            if tx.signature not in seen_signatures:
                seen_signatures.add(tx.signature)
                txs.append(tx)
    return txs