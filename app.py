import constants as keys
from telegram.ext import *
import response as r

print("Bot started")

def start(update, context):
    update.message.reply_text("Type something")
def handle_message(update, context):
    text = str(update.message.text).lower()
    responses = r.resp(text)

    update.message.reply_text(responses)

if __name__ == "__main__":
    updater = Updater(keys.API_KEY,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()
