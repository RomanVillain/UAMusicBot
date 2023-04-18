import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

BOT_TOKEN = "6146695182:AAGpz2yFs_9U-3hARDYGEeXsaCpzaicEuEQ"

# Создаем экземпляр Updater и Dispatcher
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def send_message_with_buttons(update, context):
    # Создаем кнопки
    keyboard = [[InlineKeyboardButton("Кнопка 1", callback_data='button1'),
                 InlineKeyboardButton("Кнопка 2", callback_data='button2'),
                 InlineKeyboardButton("Кнопка 3", callback_data='button3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Отправляем сообщение с кнопками
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Виберіть закладку:",
                             reply_markup=reply_markup)

def button_click(update, context):
    query = update.callback_query
    if query.data == 'button1':
        # Обработка нажатия кнопки 1
        pass
    elif query.data == 'button2':
        # Обработка нажатия кнопки 2
        pass

# Регистрируем обработчик для команды /start
start_handler = CommandHandler('start', send_message_with_buttons)
dispatcher.add_handler(start_handler)

# Регистрируем обработчик для нажатий на кнопки
button_handler = CallbackQueryHandler(button_click)
dispatcher.add_handler(button_handler)

# Запускаем бота
updater.start_polling()
