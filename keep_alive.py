from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "📡 البوت يعمل حالياً بدون مشاكل"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    thread = threading.Thread(target=run)
    thread.start()
