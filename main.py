import time
import random
from datetime import datetime
from instagrapi import Client
import os
from keep_alive import keep_alive

# إبقاء السيرفر شغال
keep_alive()

# تسجيل الدخول
cl = Client()
username = os.environ.get("INSTAGRAM_USERNAME")
password = os.environ.get("INSTAGRAM_PASSWORD")

try:
    cl.load_settings("session.json")
    cl.login(username, password)
    print("✅ تم تسجيل الدخول باستخدام الجلسة.")
except Exception:
    print("⚠️ فشل تسجيل الدخول التلقائي، تسجيل يدوي...")
    cl.login(username, password)
    cl.dump_settings("session.json")

# عرض آخر معرفات المحادثات
print("\n🧾 معرفات آخر المحادثات:")
threads = cl.direct_threads(amount=5)
for thread in threads:
    print(f"- {thread.thread_title} → {thread.id}")

# أدخل معرفات المجموعات هنا بعد نسخها من الأعلى
group_ids = [
    "ضع_هنا_معرف_المجموعة"
]

# أذكار الصباح
azkar_sabah = """☀️ *أذكار الصباح*

1. آية الكرسي (البقرة: 255)
2. بسم الله الذي لا يضر... (3 مرات)
3. أصبحنا وأصبح الملك لله...
4. سبحان الله وبحمده (100 مرة)
5. اللهم إني أسألك العفو...
6. الإخلاص والمعوذتين
7. الصلاة على النبي ﷺ
📿 اجعلها عادة صباحية تبعث الطمأنينة.
"""

# أذكار المساء
azkar_masaa = """🌙 *أذكار المساء*

1. آية الكرسي (البقرة: 255)
2. الإخلاص والمعوذتين (3 مرات)
3. بسم الله الذي لا يضر... (3 مرات)
4. أمسينا وأمسى الملك لله...
5. سبحان الله وبحمده (10 مرات)
6. اللهم إني أسألك العفو...
7. الصلاة على النبي ﷺ
💛 انشر تؤجر.
"""

# أذكار عشوائية
azkar_list = [
    "الباقيات_الصالحات\nسُبحان الله🌸.\nالحمدلله☁️.\nلا إله إلا الله 💛.\nالله أكبر 🍃.\nلاحول ولا قوة إلا بالله 🍂.\nأستغفر الله العظيم وأتوب إليه 🌺",
    "الحمد لله",
    "لا إله إلا الله",
    "الله أكبر",
    "أستغفر الله",
    "لا حول ولا قوة إلا بالله",
    "سبحان الله وبحمده",
    "اللهم صل وسلم على نبينا محمد",
]

# تتبع الإرسال
already_sent = {"morning": False, "evening": False}
last_zikr_time = time.time() - 10800  # للسماح بالإرسال فور التشغيل

# التشغيل المستمر
while True:
    now = datetime.now()
    hour = now.hour

    if hour == 6 and not already_sent["morning"]:
        for group in group_ids:
            cl.direct_send(azkar_sabah, thread_ids=[group])
        print("☀️ أُرسلت أذكار الصباح")
        already_sent["morning"] = True
        already_sent["evening"] = False

    elif hour == 18 and not already_sent["evening"]:
        for group in group_ids:
            cl.direct_send(azkar_masaa, thread_ids=[group])
        print("🌙 أُرسلت أذكار المساء")
        already_sent["evening"] = True
        already_sent["morning"] = False

    if time.time() - last_zikr_time >= 10800:
        zikr = random.choice(azkar_list)
        for group in group_ids:
            cl.direct_send(zikr, thread_ids=[group])
        print("🔁 تم إرسال ذكر:", zikr)
        last_zikr_time = time.time()

    time.sleep(60)
