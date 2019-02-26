from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem 
import datetime
logging.basicConfig(format ='%(asctime)s - %(levelname)s - %(message)s',
                    level = logging.INFO,
                    filename = 'bot.log'
                    )
def greet_user(bot, update):
   text = 'Вызван /start'
   update.message.reply_text(text)
def talk_to_me(bot, update):
   user_text = "Привет {}! Ты написал {}".format(update.message.chat.first_name,update.message.text)
   logging.info("User: %s, Chat id: %s, Message: %s",
   update.message.chat.username,update.message.chat.id,update.message.text)
   update.message.reply_text(user_text)
def get_constellation(bot, update):
   planet = update.message.text.split()[1]
   try:
      date = datetime.datetime.now()
      planet_ephem = getattr(ephem, planet)()
      planet_ephem.compute(date)
      update.message.reply_text(f'Созвездия:{ephem.constellation(planet_ephem)}')
   except AttributeError:
      update.message.reply_text(f'{planet} - это не планета!')
  
def main():
   mybot = Updater(settings.API_KEY, request_kwargs = settings.PROXY)
   logging.info('Бот запускается')
   dp = mybot.dispatcher
   dp.add_handler(CommandHandler("start",greet_user))
   dp.add_handler(MessageHandler(Filters.text, talk_to_me))
   dp.add_handler(CommandHandler("planet",get_constellation))
   mybot.start_polling()
   mybot.idle()

main()