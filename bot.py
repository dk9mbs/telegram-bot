
from uuid import uuid4
from telegram.ext import Updater, CommandHandler
import os
import datetime


def put(bot, update, user_data):
    """Usage: /put value"""
    # Generate ID and seperate value from command
    key = str(uuid4())
    value = update.message.text.partition(' ')[2]

    # Store value
    user_data[key] = value

    update.message.reply_text(key)

def get(bot, update, user_data):
    """Usage: /get uuid"""
    # Seperate ID from command
    key = update.message.text.partition(' ')[2]

    # Load value
    try:
        value = user_data[key]
        update.message.reply_text(value)

    except KeyError:
        update.message.reply_text('Not found')
        
def sunspot(bot, update, user_data):
    try:
        print(update.message.text)
        chat_id=update.message.chat_id
        print ("chatid => "+str(chat_id))

        timestamp = datetime.datetime.now().isoformat()


        bot.sendPhoto(chat_id=chat_id, photo='{0}&a={1}'.format('https://owncloud.dk9mbs.de/index.php/s/iRQLRD5caSwCwgb/download?path=%2F&files=cycles.jpg', timestamp))
        bot.sendPhoto(chat_id=chat_id, photo='{0}&a={1}'.format('https://owncloud.dk9mbs.de/index.php/s/iRQLRD5caSwCwgb/download?path=%2F&files=sunspots_last365_days.jpg', timestamp))
        bot.sendPhoto(chat_id=chat_id, photo='{0}&a={1}'.format('https://owncloud.dk9mbs.de/index.php/s/iRQLRD5caSwCwgb/download?path=%2F&files=sunspots_current_month.jpg', timestamp))


    except Exception as e:
        update.message.reply_text(str(e))


if __name__ == '__main__':
    token=os.getenv("TELEGRAMBOT_TOKEN")
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('put', put, pass_user_data=True))
    dp.add_handler(CommandHandler('get', get, pass_user_data=True))
    dp.add_handler(CommandHandler('sunspot', sunspot, pass_user_data=True))

    updater.start_polling()
    updater.idle()
