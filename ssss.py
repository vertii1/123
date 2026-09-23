from flask import Flask, request, redirect
import datetime

app = Flask(__name__)

TARGET_URL = "https://onlyfans.com" 

@app.route('/')
@app.route('/<path:path>')
def log_and_redirect(path=""):
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{time_now}] IP: {user_ip} | User-Agent: {user_agent} | Path: /{path}")

    return redirect(TARGET_URL, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)