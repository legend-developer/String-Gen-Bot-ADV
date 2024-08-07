worker: bash start
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the start command function
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hey Dear, I'm alive. Don't Worry🙃")

# Main function to set up the bot
def main() -> None:
    # Replace 'BOT_TOKEN' with your actual bot token
    updater = Updater("BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
