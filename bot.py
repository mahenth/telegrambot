import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Stupid", callback_data='stupid')],
        [InlineKeyboardButton("Fat", callback_data='fat')],
        [InlineKeyboardButton("Dumb", callback_data='dumb')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.message.chat_id, text='Please select a category:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    joke = ''
    if query.data == 'stupid':
        joke = "Why did the scarecrow win an award? Because he was outstanding in his field."
    elif query.data == 'fat':
        joke = "Why did the tomato turn red? Because it saw the salad dressing!"
    elif query.data == 'dumb':
        joke = "Why don't scientists trust atoms? Because they make up everything."
    context.bot.send_message(chat_id=query.message.chat_id, text=joke)

def main():
    updater = Updater('6004955234:AAH28Gx64PtE0Z2xkM5yHXpQ4UQKIGNxMpk', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
