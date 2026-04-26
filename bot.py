import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="မင်္ဂလာပါ မမ! Koyeb မှာ အောင်မြင်သွားပါပြီ။")

if __name__ == '__main__':
    # မမရဲ့ Token
    TOKEN = "8641830710:AAFOzSrCzHC37OOBaJLmtExFr0gAE6xb5TU"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()
  
