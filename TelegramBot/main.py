from typing import Final
from telegram import Update # pyright: ignore[reportMissingImports]
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes # pyright: ignore[reportMissingImports]



TOKE: Final = "8342961209:AAEDlLdkxK4zLJeZrAGHtKHnRNK8ONpkDpw"
BOT_USERNAME: Final = "@pythonanians_bot"

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, Thanks for chatting with me! I'm a python Expert bot.")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to help you about whatever you want about python")
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is custom command!")

# response
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if "hello" in processed:
        return "Hey, There!"
    if "how are you?" in processed:
        return "I'm good!"
    if "i love python" in processed:
        return "Remember to subscribe!"

    return "I do not understand what are you saying."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id} in {message_type}: '{text}')")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")



if __name__ == '__main__':
    print("Bot starting....")
    app = Application.builder().token(TOKE).build()


    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # errors
    app.add_error_handler(error)

    print("Polling...")
    # polls the bot
    app.run_polling(poll_interval=3)










