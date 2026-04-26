import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = '8641830710:AAFOzSrCzHC37OOBaJLmtExFr0gAE6xb5TU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("နဂါး Bot ကို အားပေးစကားတွေ ထပ်ဖြည့်ပေးလိုက်ပါပြီ မမ!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        sid = update.message.sticker.file_id
        await update.message.reply_text(f"Sticker ID ရပါပြီ မမ:\n`{sid}`", parse_mode='MarkdownV2')
        return

    text = update.message.text
    if not text: return
    text = text.lower()

    # --- ၁။ နေမကောင်းဖြစ်တာ (ဂရုစိုက်ပေးမယ့်အပိုင်း) ---
    if any(word in text for word in ["နေမကောင်းဘူး", "နေမကောင်းလို့", "ဖျားနေတယ်", "နေမသာဘူး"]):
        reply = (
            "ဟာ... မမရယ် နေမကောင်းဘူးလား။ စိတ်မကောင်းလိုက်တာ။ 😟\n\n"
            "ဆေးသောက်ပြီး အနားယူပါနော်။ အစာလည်း ဝင်အောင်စားပါ။ "
            "နဂါးက မမ အမြန်ဆုံး နေကောင်းလာဖို့ ဆုတောင်းပေးနေမယ်နော်။ ဂရုစိုက်ပါ မမ။"
        )
        await update.message.reply_text(reply)

    # --- ၂။ ပျင်းနေတယ် (စိတ်ပြေလက်ပျောက်ဖြစ်အောင်) ---
    elif any(word in text for word in ["ပျင်းတယ်", "ပျင်းနေတယ်", "ပျင်းလိုက်တာ"]):
        sticker_id = "CAACAgIAAxkBAAMhae2kivs8bOjnl3SJSqiKuqkVQwEAAn8lAAIcpchK-K0rhejI4VI7BA"
        await update.message.reply_sticker(sticker=sticker_id)
        await update.message.reply_text(
            "ပျင်းနေရင် နဂါးကို စကားလာပြောလေ... မဟုတ်ရင်လည်း သီချင်းလေး နားထောင်လိုက်ပါလား မမ။ "
            "ပျင်းတာက ပျင်းတာပဲ၊ နဂါးကတော့ မမကို ချစ်တာပဲ ဟီးး။"
        )

    # --- ၃။ အချစ်ရေးနှင့် ခံစားချက် ---
    elif any(word in text for word in ["ချစ်တယ်", "ချစ်လို့"]):
        await update.message.reply_text("ဟုတ်ကဲ့ ချစ်ပေးတဲ့အတွက် နဂါးရဲ့ ချိုချဉ်လေးတစ်လုံး ပေးပါ့မယ်နော်... ဝါးးး 🍬")

    elif any(word in text for word in ["လွမ်းတယ်", "လွမ်းလို့"]):
        await update.message.reply_text("လွမ်းတယ်ဆိုတာက အတူရှိခဲ့တဲ့ အမှတ်တရတွေ ရှိနေလို့ပေါ့... မမရယ်")

    elif any(word in text for word in ["ကံဆိုးတယ်", "ကံညံ့တယ်"]):
        await update.message.reply_text("ကံဆိုတာ အမြဲဆိုးမနေပါဘူး မမရဲ့။ အခုကံညံ့နေတာက နောက်လာမယ့် ကံကောင်းခြင်းတွေအတွက် အစပျိုးနေတာလို့ သဘောထားလိုက်ပါနော်။")

    # --- ၄။ အခေါ်အဝေါ်နှင့် နေ့စဉ်စကား ---
    elif "ကျိုးအန်းရှင်း" in text:
        await update.message.reply_text("နဂါးကိုကို ကိုခေါ်တာဘာလို့လဲ")

    elif "နဂါး" in text:
        await update.message.reply_text("ဗျာ... မမ ခေါ်လိုက်လို့ ကျွန်တော်ပြေးလာပြီ!")

    elif any(word in text for word in ["စားပြီးပြီလား", "ထမင်းစားပြီးပြီလား"]):
        await update.message.reply_text("ဟုတ်... မမကရော စားပြီးပြီလားခင်ဗျ? ဗိုက်ဝအောင်စားနော်။")

    elif any(word in text for word in ["အိပ်တော့မယ်", "goodnight"]):
        await update.message.reply_text("ဟုတ်ကဲ့ပါ မမ။ ကောင်းကောင်းအိပ်စက်အနားယူပါနော်။ အိမ်မက်လှလှမက်ပါစေ!")

    # --- ၅။ အခြားစာများ ---
    else:
        await update.message.reply_text("နဂါးလေးက ဒါကိုတော့ မသိသေးဘူးခင်ဗျာ... သင်ပေးပါဦးလား?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.run_polling()
