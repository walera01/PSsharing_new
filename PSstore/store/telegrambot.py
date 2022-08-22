# import telebot
#
# token='5312585208:AAE2lpDgQEtBy2li7wCvcJTplxxAs11LAFQ'
#
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):                    # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)
#
# if __name__ == '__main__':
#      bot.infinity_polling()
#

#!/usr/bin/env python3

import requests
#
# def send_telegram(text: str):
#     token = "5573811919:AAFM0EG5FREx2Sf5j8qf_Whb9g963ixKzAE"
#     url = "https://t.me/rotert_bot"
#     channel_id = "@rotert_bot"


# @userinfobot знать свой id


import telebot


def Send(message):
    token = '5573811919:AAFM0EG5FREx2Sf5j8qf_Whb9g963ixKzAE'
    bot = telebot.TeleBot(token)
    chatId = '417440391'
    bot.send_message(chatId, text=message)