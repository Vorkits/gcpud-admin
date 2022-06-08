
from tinydb import TinyDB, Query
import telebot
from checkup import checkup
import time


group_id=-517960140
while True:
    
    checkup_data=str(checkup.Checkup_system().check_servers_info())
    bot = telebot.TeleBot("5105468235:AAFeqSnQ4EpXsUMMfNCtcoDi9sX65lWUrfk", parse_mode=None)
    bot.send_message(group_id,checkup_data)
    time.sleep(14400)