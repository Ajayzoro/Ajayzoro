import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a file sharing bot. Send me any file and I'll upload it to my server and give you a link to download it.")

# Define the file handler
def file_handler(update, context):
    file = update.message.document
    file_name = file.file_name
    file_id = file.file_id
    file_link = context.bot.get_file(file_id).file_path
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"File uploaded: {file_name}\nDownload link: {file_link}")

# Define the error handler
def error(update, context):
    logging.error(f"Update {update} caused error {context.error}")

# Set up the bot
def main():
    # Create an updater object
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the handlers
    start_handler = CommandHandler('start', start)
    file_handler = MessageHandler(Filters.document, file_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(file_handler)

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if name == 'main':
    main()


This c





