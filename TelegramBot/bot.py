import aiohttp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import nest_asyncio

# Apply nest_asyncio for PythonAnywhere's environment
nest_asyncio.apply()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- HARDCODED CONFIGURATION (INSECURE) ---
TOKEN = "8342961209:AAGbwlQcd22cv8klvE6D3e_ThgrzknTmMjo"
BOT_USERNAME = "@pythonanians_bot"
API_KEY = "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"
MODEL = "openai/gpt-3.5-turbo"

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a Python Expert bot. Ask me anything about Python programming.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to help with Python-related questions. Just send me your Python query.")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command! Ask me about Python for more help.")

# Response handler
async def handle_response(text: str) -> str:
    system_prompt = (
        "You are a Python expert bot. Answer questions about Python programming only. "
        "If the question is not about Python, respond with: 'Sorry, I can only answer Python-related questions.' "
        "Provide clear, concise answers with code examples when appropriate."
    )
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": text}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 1000
                }
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data['choices'][0]['message']['content'].strip()
                return "Sorry, I couldn't process your request. Please try again."
        except Exception as e:
            logger.error(f"Error in handle_response: {e}")
            return "Sorry, an error occurred. Please try again."

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    logger.info(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    if message_type == "group":
        if BOT_USERNAME in text:
            text = text.replace(BOT_USERNAME, '').strip()
        else:
            return

    response = await handle_response(text)
    logger.info(f"Bot response: {response}")
    await update.message.reply_text(response)

# Error handler
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")
    if update.message:
        await update.message.reply_text("Sorry, something went wrong. Please try again.")
def main():
    """Start the bot with hardcoded configuration."""
    # Security warning
    logger.warning("RUNNING WITH HARDCODED SECRETS - NOT SAFE FOR PRODUCTION")
    
    # Create and configure application
    application = Application.builder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("custom", custom_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    # Run the bot
    logger.info("Starting polling...")
    application.run_polling()

if __name__ == '__main__':
    main()