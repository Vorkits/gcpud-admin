import telebot
import CONFIG
from pprint import pprint
import json
from checkup import checkup
from telebot import types
import threading
from tinydb import TinyDB, Query
bot = telebot.TeleBot("5105468235:AAFeqSnQ4EpXsUMMfNCtcoDi9sX65lWUrfk", parse_mode=None)
db = TinyDB('status.json')
User = Query()
def print_list(my_list):
    return '' + (', '.join(my_list))
def get_start_message():
    start_message="""
    Сервера: serverlist
    Соц сети: media
    
    Список сервер-работающие соц-сети
    servers
    """
    servers=checkup.Checkup_system()._get_servers()
    medias=checkup.Checkup_system()._get_medias()
    server_medias=checkup.Checkup_system()._get_servers_medias()   
    start_message=start_message.replace('serverlist',print_list(servers))
    start_message=start_message.replace('media',print_list(medias))
    start_message=start_message.replace('servers',json.dumps(server_medias, indent=2))

    return start_message

def check_server(tg_user_id):
    result=checkup.Checkup_system().check_servers_info()
    db.truncate()
    bot.send_message(tg_user_id,result)
def async_checkup():
    my_thread = threading.Thread(target=check_server)
    # my_thread = threading.Thread(target=print)
    my_thread.start()
    

@bot.callback_query_handler(func=lambda call: True)
def longname(call):
    if call.data == "status":
        status=checkup.Checkup_system().get_servers_info()
        if not status:
            status='ни одной проверки не найдено, запустите проверку для получения информации'
        bot.send_message(chat_id=call.message.chat.id, text=status)
    if call.data == "checkup":
        
        if checkup_status := db.search(User.checkup == 'True'):
            bot.send_message(chat_id=call.message.chat.id, text='Уже идет проверка системы, ожидайте уведомления')
        else:
            db.insert({'checkup': 'True'})
            async_checkup()
            bot.send_message(chat_id=call.message.chat.id, text='Начата проверка, ожидание результата')

@bot.message_handler(commands=['start', 'help'])    
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text='Статус серверов-соцсетей',callback_data="status"))
    # markup.add(types.InlineKeyboardButton(text='Проверить работоспособность',callback_data="checkup"))

    bot.send_message(message.chat.id, get_start_message(),reply_markup=markup)
 
 
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    pass
bot.infinity_polling()