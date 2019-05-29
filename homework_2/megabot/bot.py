from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

PROXY = {'proxy_url': 'socks5h://learn:python@t3.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

# Прикручиваем логирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'How are you?'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = f'Привет {update.message.chat.first_name}! Как ты мог написать мне {update.message.text}???'
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    print(update.message)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("825427435:AAFmGlbMbmBvkgLGZLjpWDZ6unzi08etqbU", request_kwargs=PROXY)
    
    logging.info("Bot is running")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling() #начни ходить на платформу telegram и проверять наличие сообщений
    mybot.idle() #будет выполнять пока принудитлеьноне остановим

main()


