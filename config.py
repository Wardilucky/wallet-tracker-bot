import os

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
INFURA_API_KEY = os.environ["INFURA_API_KEY"]

EVM_WALLETS = os.environ["EVM_WALLETS"].split(",")
SOLANA_WALLETS = os.environ["SOLANA_WALLETS"].split(",")

WATCHED_WALLETS = {
    "evm": EVM_WALLETS,
    "solana": SOLANA_WALLETS,
}
