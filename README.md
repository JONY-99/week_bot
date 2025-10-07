
# 🚖 Megapark Taxi WeekBot  

> Telegram kanali uchun avtomatik haftalik post yuboruvchi bot  
> Har kuni soat **06:00 (Asia/Tashkent)** da rasm va motivatsion xabar joylaydi  

---

### ✨ Tavsif

**Megapark Taxi WeekBot** — bu Telegram kanali uchun mo‘ljallangan avtomatik “haftalik xabar” bot.  
U har kuni ertalab soat **06:00** da rasm va kunlik motivatsion postni avtomatik joylaydi.  
Postlar ichida **premium emojilar**, **tasodifiy taglaynlar** va **manzil/Instagram/sayt tugmalari** mavjud.  

Haydovchilar uchun har kuni ruhiy ko‘tarinkilik va baraka tilash maqsadida yaratilgan.  

---

### 🧠 Asosiy imkoniyatlar

✅ Har kuni avtomatik ravishda kanalga post yuboradi  
✅ Haftaning 7 kuni uchun alohida matn va rasm  
✅ Inline tugmalar (lokatsiya, Instagram, sayt)  
✅ Premium emoji bilan chiroyli dizayn  
✅ `/test`, `/whereami`, `/resolve` komandalarini qo‘llab-quvvatlaydi  
✅ Log yozuvlari (success / error holatlar uchun)  

---

### 🛠 Texnologiyalar

- [Python 3.12+](https://www.python.org/)
- [python-telegram-bot v20.7](https://github.com/python-telegram-bot/python-telegram-bot)
- [pytz](https://pypi.org/project/pytz/)
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [logging](https://docs.python.org/3/library/logging.html)

---

### ⚙️ O‘rnatish

#### 1️⃣ Repository’ni clone qilish:
```bash
git clone https://github.com/<your-username>/megapark-weekbot.git
cd megapark-weekbot


python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows


python-telegram-bot[job-queue]==20.7
pytz


| Parametr        | Tavsif                                                                |
| --------------- | --------------------------------------------------------------------- |
| `BOT_TOKEN`     | Sizning Telegram bot tokeningiz (`@BotFather` dan olingan)            |
| `CHAT_ID`       | Kanal yoki guruh identifikatori (masalan `@mptaxi` yoki `-100xxxxxx`) |
| `INSTAGRAM_URL` | Instagram sahifangiz                                                  |
| `WEBSITE_URL`   | Rasmiy sayt manzili                                                   |
| `MAPS_URL`      | Lokatsiya (Google Maps link)                                          |
| `TZ`            | `Asia/Tashkent` vaqt zonasi                                           |


| Komanda     | Tavsifi                                  |
| ----------- | ---------------------------------------- |
| `/test`     | Hozir darhol post yuboradi (sinov uchun) |
| `/whereami` | Joriy chat ID va turini ko‘rsatadi       |
| `/resolve`  | Bot kanalga ulanganini tekshiradi        |


megapark-weekbot/
│
├── images/
│   ├── monday.png
│   ├── tuesday.png
│   ├── wednesday.png
│   ├── thursday.png
│   ├── friday.png
│   ├── saturday.png
│   └── sunday.png
│
├── main.py
├── requirements.txt
└── README.md


💎✨ DUSHANBA TONGI MUBORAK!

Yangi hafta – sizlarga omadli safarlar, muloyim mijozlar, tinch yo‘llar tilaymiz! 🚖💛

🌟 Bugun sizga omad tilaymiz!
📍 Bizning Manzil | 📸 Instagram | 🌐 Rasmiy saytimiz


run_time = dt.time(hour=6, minute=0, tzinfo=TZ)
app.job_queue.run_daily(daily_job, time=run_time, name="daily_post")


2025-10-07 06:00:01 | INFO | weekbot | ✅ Post yuborildi: chat_id=@mptaxi
2025-10-07 06:00:02 | ERROR | weekbot | ❌ Post yuborishda xato: Chat not found


python main.py


2025-10-07 06:00:00 | INFO | weekbot | 🚀 Bot start…
2025-10-07 06:00:00 | INFO | weekbot | ⏲️ Job sched: 06:00 Asia/Tashkent
2025-10-07 06:00:00 | INFO | weekbot | 📡 Polling boshlanyapti…


<p align="center"> Made with 💛 for Megapark Taxi Drivers 🚖 </p> ```