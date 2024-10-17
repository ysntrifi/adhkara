import time
from instabot import Bot

bot = Bot()
bot.login(username="bot_adhkar", password="@YsnTrifi10")

sent_messages = {}

def send_dhikr(user_id):
    dhikr_message = "سبحان الله وبحمده، سبحان الله العظيم"
    bot.send_message(dhikr_message, [user_id])
    print(f"بعثت ذكر لـ {user_id}")

def check_and_send(user_id):
    current_day = time.strftime("%Y-%m-%d")
    if user_id not in sent_messages or sent_messages[user_id] != current_day:
        send_dhikr(user_id)
        sent_messages[user_id] = current_day

def monitor_group():
    messages = bot.get_messages()
    for message in messages:
        user_id = message['user_id']
        check_and_send(user_id)

while True:
    monitor_group()
    time.sleep(60)