from .extra_func import get_url
import time

class Telegram_Bot(object):
    def __init__(self, bot_id="1133081716:AAE0XRj-w5wmsj4g_-RKVSx2rKixDfolgdM"):
        self.bot_id = bot_id
        self.url = "https://api.telegram.org/bot"+bot_id+"/"

    def send_msg(self, text, chat_id):
        try:
            send_msg = self.url + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, chat_id, 'markdown')
            ret_val = get_url(send_msg)
            try:
                cause = ret_val["description"]
                if cause.find("Too Many Requests:") != -1:
                    print("Too many requests! Waiting...")
                    time.sleep(20)
                    ret_val = get_url(send_msg)
                    print(ret_val)
                else:
                    print(ret_val)
            except Exception as e1:
                x = e1.args
                print("Message sent successfully")
        except Exception as e:
            print(type(e))
            print(e.args)

    def last_msg(self):
        try:
            updates = self.url+"getupdates"
            ret_val = get_url(updates)
            last_msg = ret_val['result'][0]
            return last_msg
        except Exception as e:
            print(e.args)
