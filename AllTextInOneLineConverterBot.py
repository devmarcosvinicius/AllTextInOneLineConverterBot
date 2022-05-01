import telegram.ext
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
)
from telegram import ParseMode, Update

API_KEY = "API_KEY GOES HERE"
updater = Updater(API_KEY, use_context=True)
bot = updater.bot


def startCommand(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Paste the text here: ")


def helpCommand(update: Update, context: CallbackContext):
    bot.sendMessage(
        update.message.chat_id,
        """
I'm a bot created for convert texts with multiple lines in a single                       line text.
E.G.\n
  From:
    A B C
    C D E
    F G H\n
  To:
    A B C D E F G H\n
Usage: Just paste and enter the text. At the end you can just click on  the text to copy.\n
                  
I was made by @marcosderek
                  """,
    )


def reply(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text="`" + update.message.text.replace("\n", " ") + "`",
        parse_mode=ParseMode.MARKDOWN,
    )

    bot.sendMessage(update.message.chat_id, "Click on the text to copy.")


def main() -> None:
    updater.dispatcher.add_handler(CommandHandler("start", startCommand))
    updater.dispatcher.add_handler(CommandHandler("help", helpCommand))

    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()

main()
