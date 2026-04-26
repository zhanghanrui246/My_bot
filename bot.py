import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# မမရဲ့ Token ကို အမှန်အတိုင်း ထည့်ပေးထားပါတယ်
TOKEN = '8641830710:AAFOzSrCzHC37OOBaJLmtExFr0gAE6xb5TU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("နဂါး Bot လေး အဆင်သင့်ဖြစ်ပါပြီ မမ!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if not text: return
    text = text.lower()

    if any(word in text for word in ["နေမကောင်းဘူး", "ဖျားနေတယ်"]):
        await update.message.reply_text("ဆေးသောက်ပြီး အနားယူပါနော် မမ။ နဂါးက စိတ်ပူလို့ပါ။ 😟")
    elif any(word in text for word in ["ပျင်းတယ်", "ပျင်းနေတယ်"]):
        await update.message.reply_text("နဂါးရှိပါသေးတယ်... ဘဝက တိုတိုလေးပါ၊ ချစ်ကြည့်ပါ နဂါးကို! 🐉")
    elif "နဂါး" in text:
        await update.message.reply_text("ဗျာ... မမ ခေါ်လိုက်လို့ ကျွန်တော်ပြေးလာပြီ!")
    else:
        await update.message.reply_text("မမ ပြောတာလေး နားထောင်နေပါတယ်ရှင်...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
    
