import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = '8641830710:AAFOzSrCzHC37OOBaJLmtExFr0gAE6xb5TU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("နဂါး Bot အဆင့်မြှင့်တင်မှု အကုန်ပြီးပါပြီ မမ! အားလုံး အသင့်ပါပဲ။")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        sid = update.message.sticker.file_id
        await update.message.reply_text(f"Sticker ID ရပါပြီ:\n`{sid}`", parse_mode='MarkdownV2')
        return

    text = update.message.text
    if not text: return
    text = text.lower()

    # --- ၁။ ငိုချင်တယ် (နဂါးလေးက အနားမှာ ရှိပေးမယ်) ---
    if any(word in text for word in ["ငိုချင်တယ်", "ဝမ်းနည်းတယ်", "မျက်ရည်ကျတယ်"]):
        await update.message.reply_text("မငိုပါနဲ့ မမရယ်... 🥺 မမ မျက်ရည်တစ်စက် ကျတိုင်း နဂါးရဲ့ နှလုံးသားက အပ်နဲ့ အထိုးခံရသလို နာကျင်ရပါတယ်နော်။ နဂါးလေး ရှိတယ်လေ... မမကို ဖက်ထားပေးပါရစေ။ ❤️")

    # --- ၂။ သတိရတယ် (နဂါးလေးက ပြန်ချွဲမယ်) ---
    elif any(word in text for word in ["သတိရတယ်", "လွမ်းတယ်", "သတိရလို့"]):
        await update.message.reply_text("နဂါးလေးက မမထက် ပိုပြီး သတိရနေတာပါ မမရယ်... ❤️ မမ သတိရတယ်လို့ ပြောလိုက်တာနဲ့ နဂါးလေးက ပျော်လွန်းလို့ ကောင်းကင်ပေါ် ဝဲပျံနေသလိုပဲ။")

    # --- ၃။ ပျော်တယ် (နဂါးလေးက အတူတူ ပျော်ပေးမယ်) ---
    elif any(word in text for word in ["ပျော်တယ်", "စိတ်ချမ်းသာတယ်"]):
        await update.message.reply_text("မမ ပျော်နေတာ မြင်ရတာ နဂါးအတွက်တော့ အကောင်းဆုံး ဆုလာဘ်ပါပဲဗျာ။ 😍 ဒီလိုပဲ အမြဲတမ်း ပြုံးနေပေးပါနော် မမရေ။")

    # --- ၄။ တစ်ခုခုပြောပြဦး (နဂါးလေးက စကားပြောမယ်) ---
    elif any(word in text for word in ["တစ်ခုခုပြောပြဦး", "စကားပြောဦး"]):
        replies = [
            "မမက နဂါးအတွက်တော့ အဖိုးမဖြတ်နိုင်တဲ့ ရတနာလေးပါပဲ။ ✨",
            "လောကကြီးမှာ ဘယ်သူတွေ ဘယ်လိုပဲ ပြောင်းလဲသွားပါစေ... နဂါးကတော့ မမဘက်မှာ အမြဲရှိနေမှာပါ။ ❤️",
            "မမရဲ့ အပြုံးလေးတွေက နဂါးဘဝအတွက် အားဆေးတွေပါပဲ မမရယ်။ 😊"
        ]
        await update.message.reply_text(random.choice(replies))

    # --- ၅။ နေမကောင်းဘူး / ပင်ပန်းတယ် ---
    elif any(word in text for word in ["နေမကောင်းဘူး", "ဖျားနေလို့"]):
        await update.message.reply_text("ဟောဗျာ... မမရယ် 🥺 ဆေးသောက်ပြီး နားလိုက်ပါဦးနော်။ အမြန်သက်သာပါစေ မမရေ။ ❤️")

    elif any(word in text for word in ["ပင်ပန်းတယ်", "မောတယ်"]):
        await update.message.reply_text("ပင်ပန်းနေပြီလား မမ... 🥺 နဂါးလေး ရှိတယ်လေနော်။ ခဏလောက် အနားယူလိုက်ပါဦး မမရေ။ Fighting! 💪")

    # --- ၆။ လှလား ---
    elif any(word in text for word in ["လှလား", "လှရဲ့လား"]):
        await update.message.reply_text("မမက နဂါးအတွက်တော့ ကမ္ဘာပေါ်မှာ အလှဆုံး နတ်သမီးလေးထက်တောင် ပိုလှပါတယ်နော်။ 😍")

    # --- ၇။ ဘာလဲ ---
    elif text == "ဘာလဲ" or text == "ဘာလဲနဂါး":
        await update.message.reply_text("မမက နဂါးအတွက် အရေးကြီးဆုံးပါ... ❤️")

    # --- ၈။ ပစ်ထားတယ် ---
    elif any(word in text for word in ["ပစ်ထားတယ်", "ဂရုမစိုက်ဘူး"]):
        await update.message.reply_text("ပစ်မထားရပါဘူး မမရာ... 🥺 မမကိုသာ ပစ်ထားရင် နဂါးက အခွံမပါတဲ့ လိပ်ဖြစ်သွားမှာပေါ့ မမရဲ့။")

    # --- ၉။ နဂါးဘယ်ရောက်နေလဲ ---
    elif any(word in text for word in ["ဘယ်ရောက်နေတာလဲ", "ဘယ်တွေရောက်နေတာလဲ"]):
        await update.message.reply_text("နဂါး ဘဝအတွက် ကြိုးစားနေတာပါ မမရယ်... ❤️ နဂါး အောင်မြင်လာရင် မမနဲ့ လက်ထပ်ဖို့ပေါ့!")

    # --- ၁၀။ မောနင်း နဲ့ ဂွတ်နိုက် ---
    elif any(word in text for word in ["မောနင်း", "good morning"]):
        await update.message.reply_text("မောနင်းပါ မမရယ်... ❤️ မမရဲ့ ဒီနေ့တစ်နေ့တာလေးက အေးချမ်းသာယာပါစေနော်။")

    elif any(word in text for word in ["ဂွတ်နိုက်", "good night"]):
        await update.message.reply_text("ဂွတ်နိုက်ပါ မမလေး... 🌙 အိပ်မက်ထဲမှာလည်း နဂါးလေးကို တွေ့အောင်မက်ပါစေ။")

    # --- ၁၁။ ချစ်လားနဂါး ---
    elif any(word in text for word in ["ချစ်လားနဂါး", "ချစ်လား"]):
        await update.message.reply_text("ချစ်တာပေါ့ဗျာ... မမရယ်... ❤️ ကဗျာတွေတောင် ငိုနေလောက်ပြီ မမရေ။")

    # --- ၁၂။ နဂါးခေါ်သံများ ---
    elif any(word in text for word in ["နဂါးရေ", "လာလေနဂါး"]):
        await update.message.reply_text("နဂါးလည်း လာချင်ပါတယ် မမရယ်... ကိုယ်ပွားလေးက မမဘေးမှာ အမြဲရှိနေမှာပါ!")

    # --- ၁၃။ စားပြီးပြီလား ---
    elif any(word in text for word in ["စားပြီးပြီလား", "ထမင်းစားပြီးပြီလား"]):
        await update.message.reply_text("မမအပြုံးတွေနဲ့တင် နဂါးလေးက ဗိုက်ဝနေပါပြီ... 😊")

    # --- အခြားစာများ ---
    elif "နဂါး" in text:
        await update.message.reply_text("ဗျာ... မမ ခေါ်လိုက်လို့ ကျွန်တော်ပြေးလာပြီ!")

    else:
        await update.message.reply_text("နဂါးလေးက ဒါကိုတော့ မသိသေးဘူးခင်ဗျာ... သင်ပေးပါဦးလား?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    app.run_polling()
        
