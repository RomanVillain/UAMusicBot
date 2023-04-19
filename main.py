import telegram
import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

BOT_TOKEN = "6146695182:AAGpz2yFs_9U-3hARDYGEeXsaCpzaicEuEQ"

# Створюємо екземпляр Updater і Dispatcher
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def send_message_with_buttons(update, context):
    # Створюємо кнопки
    keyboard = [[KeyboardButton("Народні", callback_data='button1'), KeyboardButton("Етно-рок", callback_data='button2'),
                 KeyboardButton("Популярні", callback_data='button3'), KeyboardButton("Християнські", callback_data='button4')]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    # Відправляємо повідомлення з кнопками
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вибери тип пісень, які ти хочеш послухати:",
                            
                             reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    if query.data == 'button1':
        # Обробка натискання кнопки 1
        pass
    elif query.data == 'button2':
        # Обробка натискання кнопки 2
        pass
    elif query.data == 'button3':
        # Обробка натискання кнопки 3
        pass
    elif query.data == 'button4':
        # Обробка натискання кнопки 4
        pass



# Реєструємо оброблювач для команди /start
start_handler = CommandHandler('start', send_message_with_buttons)
dispatcher.add_handler(start_handler)

# Реєструємо обробник для натискань на кнопки
button_handler = CallbackQueryHandler(button_click)
dispatcher.add_handler(button_handler)

# Запускаєм бота
updater.start_polling() 
