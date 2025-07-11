from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN
from evm_tracker import check_evm_transactions
from solana_tracker import check_solana_transactions
from web3 import Web3
import asyncio

CHAT_ID = None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CHAT_ID
    CHAT_ID = update.effective_chat.id
    await context.bot.send_message(chat_id=CHAT_ID, text="Bot aktif. Memantau transaksi wallet...")

async def polling_task(application):
    global CHAT_ID
    while True:
        if CHAT_ID:
            for tx in check_evm_transactions():
                msg = f"[EVM] {tx['from']} → {tx['to']} | {Web3.fromWei(tx['value'], 'ether')} ETH"
                await application.bot.send_message(chat_id=CHAT_ID, text=msg)

            for tx in check_solana_transactions():
                msg = f"[Solana] Slot {tx.slot} | Tx: {str(tx.signature)[:20]}..."
                await application.bot.send_message(chat_id=CHAT_ID, text=msg)
        await asyncio.sleep(30)

async def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.start()
    asyncio.create_task(polling_task(application))
    await application.idle()

if __name__ == "__main__":
    asyncio.run(main())
