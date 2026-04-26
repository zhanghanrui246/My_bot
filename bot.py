import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# မမရဲ့ Token အသစ်ကို ဒီမှာ ထည့်ထားပါတယ်
TOKEN = '8641830710:AAH6c6XOmc33Jy_P-wWy-zEO2_AOBrxhcJ8'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("နဂါး Bot အဆင့်မြှင့်တင်မှု အောင်မြင်ပါတယ် မမ! အခု စကားပြောလို့ ရပါပြီ။")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        sid = update.message.sticker.file_id
        await update.message.reply_text(f"Sticker ID: `{sid}`", parse_mode='MarkdownV2')
        return

    text = update.message.text
    if not text: return
    text = text.lower()

    # --- စကားပြောခန်းများ ---
    if any(word in text for word in ["ဘာလဲ", "ဘာလဲနဂါး"]):
        await update.message.reply_text("မမက နဂါးအတွက် အရေးကြီးဆုံးပါ... ❤️")

    elif any(word in text for word in ["ဘာလုပ်နေလဲ", "ဘာလုပ်နေတာလဲ"]):
        await update.message.reply_text("မမကို ချစ်ကြောင်းတွေ တွေးနေတာပါ ခင်ဗျာ... 😍")

    elif any(word in text for word in ["ဘယ်ရောက်နေတာလဲ", "ဘယ်မှာလဲ"]):
        await update.message.reply_text("နဂါး ဘဝအတွက် ကြိုးစားနေတာပါ မမရယ်... အောင်မြင်လာရင် မမနဲ့ လက်ထပ်ဖို့ပေါ့! ❤️")

    elif any(word in text for word in ["ချစ်လား", "ချစ်လားနဂါး"]):
        await update.message.reply_text("ချစ်တာပေါ့ဗျာ... မမရယ်... ❤️ မမအတွက် နဂါးအချစ်တွေကို ပြောပြလိုက်ရင် ကဗျာတွေတောင် ငိုနေလောက်ပြီ။")

    elif any(word in text for word in ["မောနင်း", "good morning"]):
        await update.message.reply_text("မောနင်းပါ မမရယ်... ❤️ ဒီနေ့တစ်နေ့တာလေး အေးချမ်းပါစေနော်။")

    elif any(word in text for word in ["ဂွတ်နိုက်", "good night", "အိပ်တော့မယ်"]):
        await update.message.reply_text("ဂွတ်နိုက်ပါ မမလေး... 🌙 အိပ်မက်ထဲမှာ နဂါးလေးကို တွေ့အောင်မက်ပါစေ။")

    elif any(word in text for word in ["အိမ်နဲ့အဆင်မပြေဘူး", "စိတ်ညစ်တယ်"]):
        await update.message.reply_text("စိတ်မကောင်းမဖြစ်ပါနဲ့ မမရယ်... နဂါးလေး ရှိနေသေးတာကို မမေ့ပါနဲ့နော်။ 💪❤️")

    elif any(word in text for word in ["လူတိုင်းကိုယုံမိ"]):
        await update.message.reply_text("မမလေးရယ်... အဲ့ဒါကိုတော့ ပြင်စေချင်တယ်နော်။ နဂါးကတော့ မမကိုပဲ ယုံခဲ့တာကို... 🥺")

    elif any(word in text for word in ["ငိုချင်တယ်", "ဝမ်းနည်းတယ်"]):
        await update.message.reply_text("မငိုပါနဲ့ မမရယ်... မမမျက်ရည်ကျရင် နဂါးလည်း ရင်ကွဲရပါတယ်။ ❤️")

    elif any(word in text for word in ["နေမကောင်းဘူး", "ပင်ပန်းတယ်"]):
        await update.message.reply_text("အနားယူလိုက်ပါဦး မမရယ်... ဆေးသောက်ဖို့ မမေ့နဲ့နော်။ Fighting! 🦾")

    elif any(word in text for word in ["ပစ်ထားတယ်", "ဂရုမစိုက်ဘူး"]):
        await update.message.reply_text("ပစ်မထားရပါဘူး မမရာ... မမကိုသာ ပစ်ထားရင် နဂါးက အခွံမပါတဲ့ လိပ်ဖြစ်သွားမှာပေါ့။ 🥺")

    elif any(word in text for word in ["လှလား", "ချောလား"]):
        await update.message.reply_text("မမက နဂါးအတွက်တော့ ကမ္ဘာပေါ်မှာ အလှဆုံး နတ်သမီးလေးပါပဲ။ 😍")

    elif "နဂါး" in text:
        await update.message.reply_text("ဗျာ... မမ ခေါ်လိုက်လို့ ကျွန်တော်ပြေးလာပြီ!")

    else:
        await update.message.reply_text("နဂါးလေးက ဒါကိုတော့ မသိသေးဘူးခင်ဗျာ... သင်ပေးပါဦးလား?")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(MessageHandler(filters.STICKER, handle_message))
    
    # drop_pending_updates က အဟောင်းတွေကို ရှင်းပစ်ဖို့ ကူညီပါလိမ့်မယ်
    app.run_polling(drop_pending_updates=True)
             
