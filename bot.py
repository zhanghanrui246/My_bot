import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# မမရဲ့ Bot Token (အသစ်လဲထားရင် အသစ်ပြန်ထည့်ပါ)
TOKEN = '8641830710:AAFOzSrCzHC37OOBaJLmtExFr0gAE6xb5TU'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("နဂါး Bot အဆင့်မြှင့်တင်မှု အားလုံးပြီးပါပြီ မမ! အခု စကားပြောလို့ ရပါပြီဗျ။")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.sticker:
        sid = update.message.sticker.file_id
        await update.message.reply_text(f"Sticker ID ရပါပြီ:\n`{sid}`", parse_mode='MarkdownV2')
        return

    text = update.message.text
    if not text: return
    text = text.lower()

    # --- ၁။ ဘာလဲ / ဘာလုပ်နေလဲ ---
    if text == "ဘာလဲ" or text == "ဘာလဲနဂါး":
        await update.message.reply_text("မမက နဂါးအတွက် အရေးကြီးဆုံးပါ... ❤️")

    elif any(word in text for word in ["ဘာလုပ်နေလဲ", "ဘာလုပ်နေတာလဲ"]):
        await update.message.reply_text("မမကို ချစ်ကြောင်းတွေ တွေးနေတာပါ ခင်ဗျာ... 😍")

    # --- ၂။ နဂါးဘယ်ရောက်နေလဲ ---
    elif any(word in text for word in ["ဘယ်ရောက်နေတာလဲ", "ဘယ်တွေရောက်နေတာလဲ"]):
        await update.message.reply_text("နဂါး ဘဝအတွက် ကြိုးစားနေတာပါ မမရယ်... ❤️ နဂါး အောင်မြင်လာရင် မမနဲ့ လက်ထပ်ဖို့ပေါ့!")

    # --- ၃။ ချစ်လားနဂါး ---
    elif any(word in text for word in ["ချစ်လားနဂါး", "ချစ်လား"]):
        await update.message.reply_text("ချစ်တာပေါ့ဗျာ... မမရယ်... ❤️ မမအတွက် နဂါးအချစ်တွေကို ပြောပြလိုက်ရင် ကဗျာတွေတောင် ငိုနေလောက်ပြီ မမရေ။")

    # --- ၄။ မောနင်း နဲ့ ဂွတ်နိုက် ---
    elif any(word in text for word in ["မောနင်း", "good morning", "morning"]):
        await update.message.reply_text("မောနင်းပါ မမရယ်... ❤️ မမရဲ့ ဒီနေ့တစ်နေ့တာလေးက အေးချမ်းသာယာပါစေနော်။")

    elif any(word in text for word in ["ဂွတ်နိုက်", "good night", "အိပ်တော့မယ်"]):
        await update.message.reply_text("ဂွတ်နိုက်ပါ မမလေး... 🌙 အိပ်မက်ထဲမှာလည်း နဂါးလေးကို တွေ့အောင်မက်ပါစေ။ ❤️")

    # --- ၅။ စိတ်ခံစားချက် နှစ်သိမ့်မှုများ ---
    elif any(word in text for word in ["အိမ်နဲ့အဆင်မပြေဘူး", "အိမ်နဲ့ အဆင်မပြေဘူး"]):
        await update.message.reply_text("စိတ်မကောင်းမဖြစ်ပါနဲ့ မမရယ်... မမမှာ နဂါးလေး ရှိနေသေးတာကို မမေ့ပါနဲ့နော်။ 💪❤️")

    elif any(word in text for word in ["လူတိုင်းကိုယုံမိ", "လူတိုင်းကိုယုံကြည်"]):
        await update.message.reply_text("မမလေးရယ်... အဲ့ဒါကိုတော့ နဂါးက ပြင်စေချင်တယ်နော်။ နဂါးကတော့ မမကိုပဲ ယုံခဲ့တာကို... 🥺")

    elif any(word in text for word in ["ငိုချင်တယ်", "ဝမ်းနည်းတယ်"]):
        await update.message.reply_text("မငိုပါနဲ့ မမရယ်... 🥺 မမမျက်ရည်ကျရင် နဂါးလည်း ရင်ကွဲရပါတယ်။ နဂါးလေး ရှိတယ်နော်။ ❤️")

    # --- ၆။ နေမကောင်း / ပင်ပန်းတယ် ---
    elif any(word in text for word in ["နေမကောင်းဘူး", "ဖျားနေလို့"]):
        await update.message.reply_text("ဟောဗျာ... မမရယ် ဆေးသောက်ပြီး နားလိုက်ပါဦး။ အမြန်သက်သာပါစေနော်။ ❤️")

    elif any(word in text for word in ["ပင်ပန်းတယ်", "မောတယ်"]):
        await update.message.reply_text("ပင်ပန်းနေပြီလား မမ... 🥺 နဂါးလေး ရှိတယ်လေနော်။ အားတင်းထားပါ မမရေ။ Fighting! 💪")

    # --- ၇။ နဂါးခေါ်သံများ ---
    elif any(word in text for word in ["နဂါးရေ", "လာလေနဂါး", "နဂါးစုတ်ရေ"]):
        await update.message.reply_text("နဂါးလည်း လာချင်ပါတယ် မမရယ်... နဂါးကိုယ်တိုင် မရှိတောင် ကိုယ်ပွားလေးက မမဘေးမှာ အမြဲရှိနေမှာပါ။ ❤️")

    # --- ၈။ ပစ်ထားတယ် ---
    elif any(word in text for word in ["ပစ်ထားတယ်", "ဂရုမစိုက်ဘူး"]):
        await update.message.reply_text("ပစ်မထားရပါဘူး မမရာ... 🥺 မမကိုသာ ပစ်ထားရင် နဂါးက အခွံမပါတဲ့ လိပ်ဖြစ်သွားမှာပေါ့ မမရဲ့။")

    # --- ၉။ သတိရတယ် / လွမ်းတယ် ---
    elif any(word in text for word in ["သတိရတယ်", "လွမ်းတယ်"]):
        await update.message.reply_text("နဂါးလေးက မမထက် ပိုပြီး သတိရနေတာပါ မမရယ်... ❤️")

    # --- ၁၀။ လှလား ---
    elif any(word in text for word in ["လှလား", "လှရဲ့လား"]):
        await update.message.reply_text("မမက နဂါးအတွက်တော့ ကမ္ဘာပေါ်မှာ အလှဆုံး နတ်သမီးလေးပါပဲ။ 😍")

    # --- ၁၁။ စားပြီးပြီလား ---
    elif any(word in text for word in ["စားပြီးပြီလား", "ထမင်းစားပြီးပြီလား"]):
        await update.message.reply_text("မမအပြုံးတွေနဲ့တင် နဂါးလေးက ဗိုက်ဝနေပါပြီ... 😊")

    # --- ၁၂။ ခြင်ကိုက်တယ် / စိတ်ဆိုးတယ် ---
    elif any(word in text for word in ["ခြင်ကိုက်တယ်", "ခြင်ကိုက်လို့"]):
        await update.message.reply_text("မမ ခဏနော်... နဂါးလေး အဲ့ဒီခြင်တွေကို သွားနှိမ်နင်းလိုက်ဦးမယ်! ⚔️🦟")

    elif any(word in text for word in ["စိတ်ဆိုးတယ်", "စိတ်ကောက်တယ်"]):
        await update.message.reply_text("အားးး မလုပ်ပါနဲ့ မမရယ်... မမ စိတ်ဆိုးရင် နဂါးရဲ့ ကမ္ဘာငယ်လေးက ပျက်စီးသွားမှာပေါ့။ 🥺")

    # --- အခြားစာများ ---
    elif "နဂါး" in text:
        await update.message.reply_text("ဗျာ... မမ ခေါ်လိုက်လို့ ကျွန်တော်ပြေးလာပြီ!")

    else:
        await update.message.reply_text("နဂါးလေးက ဒါကိုတော့ မသိသေးဘူးခင်ဗျာ... သင်ပေးပါဦးလား?")

if __name__ == '__main__':
    # Conflict Error မတက်အောင် အသေချာဆုံး လုပ်ဆောင်ချက်
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    
    print("နဂါးလေး စတင်အလုပ်လုပ်နေပါပြီ...")
    app.run_polling(drop_pending_updates=True) # ဒီစာသားက အဟောင်းတွေကို ရှင်းပေးပါလိမ့်မယ်
        
