import datetime as dt
import logging
import os
import random
from pytz import timezone
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputFile, Update, Bot
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# ===== LOGGING =====
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")
log = logging.getLogger("weekbot")

# ===== CONFIG =====
BOT_TOKEN = "8395599976:AAHAWuWnoGleKK9c1Pn3bAGUUK9f1cDspb0"          # sizniki
CHAT_ID   = "@TaxiMegapark"           # gruppa ID ( /whereami bilan tekshiring )
INSTAGRAM_URL = "https://www.instagram.com/mega_park_taxi?utm_source=ig_web_button_share_sheet&igsh=Ymo1bWhscDR3aWN2"
WEBSITE_URL   = "https://megaparktaxi.uz"
MAPS_URL      = "https://maps.app.goo.gl/8UAnRpQEXkYKJgjy7"
TZ = timezone("Asia/Tashkent")

# async def verify_access():
#     bot = Bot(BOT_TOKEN)
#     me = await bot.get_me()
#     cm = await bot.get_chat_member(CHAT_ID, me.id)

#     if cm.status == "administrator":
#         print("✅ Bot kanalga admin sifatida ulangan!")
#         await bot.send_message(
#             chat_id=CHAT_ID,
#             text="💎✅ Bot muvaffaqiyatli ulandi va kanalga yozish huquqiga ega!",
#         )
#     else:
#         print(f"⚠️ Bot status: {cm.status} — hali admin emas.")
        


WEEKLY_CONTENT = {
    0: {
        "text": "💎✨ DUSHANBA TONGI MUBORAK! Yangi hafta – sizlarga omadli safarlar, muloyim mijozlar, tinch yo‘llar tilaymiz! 🚖💛",
        "image": "images/monday.png"
    },
    1: {
        "text": "🚀💫 SESHANBA MUBORAK!  Yo‘l sizni kutyapti, rul sizni sog‘ingan. 🌈 Bugungi safaringiz ham baraka bilan to‘lsin! 💪🚖",
        "image": "images/tuesday.png"
    },
    2: {
        "text": "💫🌟 CHORSHANBA MUBORAK!  Haftaning o‘rtasi – to‘xtamaslik va harakatda bo‘lish vaqti! 🔥 Bugun omad siz bilan bo‘lsin! 🚕💛",
        "image": "images/wednesday.png"
    },
    3: {
        "text": "🌿💚 PAYSHANBA MUBORAK! Bugungi kuningiz mijozlarga, safarlaringiz esa omadga to‘la bo‘lsin! ✨🚖💛",
        "image": "images/thursday.png"
    },
    4: {
        "text": "💎🤍 JUMA MUBORAK, GURUH AZOLARI!\n\nBugun har bir buyurtma sizga rizq, har bir safar tinchlik olib kelsin! 🕊️🚖💛",
        "image": "images/friday.png"
    },
    5: {
        "text": "🌈💎 SHANBA MUBORAK! Dam oling, kuch to‘plang, yangi safarlarga tayyorlaning. 😌 Tinchlik va baraka siz bilan bo‘lsin! 🚖✨",
        "image": "images/saturday.png"
    },
    6: {
        "text": "☕💎 YAKSHANBA MUBORAK!\n\nBugun xotirjamlik, shukronalik va yangilanish kuni. 🌤 Yangi haftaga kuch va ilhom bilan kirish uchun dam oling! 🚖💛",
        "image": "images/sunday.png"
    },
}

EXTRA_TAGLINES = [
    "🌟 Bugun sizga omad tilaymiz!",
    "💰 Ko‘p daromadli kun bo‘lsin!",
    "🤝 Biz g‘amxo‘rmiz va yoningizdamiz.",
    "📈 Kuningiz barakali o‘tsin!",
]

def build_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📍 Bizning Manzil",  url=MAPS_URL)],
        [InlineKeyboardButton("📸 Instagram", url=INSTAGRAM_URL)],
        [InlineKeyboardButton("🌐 Rasmiy saytimiz", url=WEBSITE_URL)],
    ])

async def post_today(context_or_app):
    # context_or_app: JobQueue context bo‘lsa context.application, /test dan bo‘lsa context.application
    app = getattr(context_or_app, "application", None) or context_or_app
    today_idx = dt.datetime.now(TZ).weekday()
    content = WEEKLY_CONTENT.get(today_idx)
    if not content:
        log.warning("Kontent topilmadi (weekday=%s)", today_idx)
        return

    caption = f"{content['text']}\n\n{random.choice(EXTRA_TAGLINES)}"
    kb = build_keyboard()
    img = content["image"]

    try:
        if os.path.exists(img):
            log.info("Lokal rasm: %s", img)
            with open(img, "rb") as f:
                await app.bot.send_photo(chat_id=CHAT_ID, photo=InputFile(f), caption=caption,
                                         parse_mode=ParseMode.HTML, reply_markup=kb)
        else:
            log.info("URL rasm: %s", img)
            await app.bot.send_photo(chat_id=CHAT_ID, photo=img, caption=caption,
                                     parse_mode=ParseMode.HTML, reply_markup=kb)
        log.info("✅ Post yuborildi: chat_id=%s", CHAT_ID)
    except Exception as e:
        log.exception("❌ Post yuborishda xato: %s", e)

# —— Handlers ——

async def daily_job(context: ContextTypes.DEFAULT_TYPE):
    log.info("⏰ Daily job 06:00 ishga tushdi")
    await post_today(context)

async def cmd_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.info("/test → from_chat_id=%s", update.effective_chat.id if update.effective_chat else None)
    await post_today(context)
    

async def cmd_whereami(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    log.info("/whereami → id=%s title=%s type=%s", chat.id, getattr(chat, "title", None), chat.type)
    await update.message.reply_text(f"📌 Chat id: `{chat.id}`\nTitle: {getattr(chat,'title',None)}\nType: {chat.type}",
                                    parse_mode=ParseMode.MARKDOWN)

async def cmd_resolve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat = await context.bot.get_chat(CHAT_ID)
        log.info("/resolve OK → id=%s title=%s type=%s", chat.id, getattr(chat,'title',None), chat.type)
        await update.message.reply_text(f"✅ CHAT_ID OK:\n- id: {chat.id}\n- title: {getattr(chat,'title',None)}\n- type: {chat.type}")
    except Exception as e:
        log.exception("/resolve xato: %s", e)
        await update.message.reply_text(f"❌ Resolve error: {e}")

def main():
    log.info("🚀 Bot start…")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    # Verify bot access to channel
     
    # asyncio.run(verify_access())
    app.add_handler(CommandHandler("test", cmd_test))
    app.add_handler(CommandHandler("whereami", cmd_whereami))
    app.add_handler(CommandHandler("resolve", cmd_resolve))

    # JobQueue (06:00 Asia/Tashkent)
    run_time = dt.time(hour=4, minute=55, tzinfo=TZ)
    app.job_queue.run_daily(daily_job, time=run_time, name="daily_post")
    log.info("⏲️ Job sched: 06:00 Asia/Tashkent")

    log.info("📡 Polling boshlanyapti…")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
