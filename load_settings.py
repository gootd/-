from instagrapi import Client

# ✏️ ضع هنا بيانات حسابك
USERNAME = "he_di.ed"
PASSWORD = "@Goot3363"

cl = Client()

try:
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings("session.json")
    print("✅ تم تسجيل الدخول وحفظ الجلسة في session.json")
except Exception as e:
    print("❌ فشل تسجيل الدخول:", e)
