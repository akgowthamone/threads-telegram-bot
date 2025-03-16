import os
import requests
from telegram import Update, InputMediaPhoto, InputMediaVideo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7395901790:AAH9QAtw9ooMsmOcXTWczBrtMm9igZM2pv0"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Welcome to Threads Downloader Bot! Send a Threads post link to download.")

async def download_threads_media(update: Update, context: CallbackContext):
    url = update.message.text
    if "threads.net" not in url:
        await update.message.reply_text("Please send a valid Threads post link.")
        return

    try:
        # Replace this with an actual Threads media downloader API
        response = requests.get(f"https://api.example.com/download?url={url}")

        if response.status_code == 200:
            data = response.json()
            media_url = data.get("media_url")

            if data.get("is_video"):
                await update.message.reply_video(media_url)
            else:
                await update.message.reply_photo(media_url)
        else:
            await update.message.reply_text("Failed to download. Make sure the post is public.")
    
    except Exception as e:
        await update.message.reply_text("An error occurred while downloading.")
        print(f"Error: {e}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_threads_media))

    app.run_polling()

if __name__ == "__main__":
    main()
