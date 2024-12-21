import os
from io import BytesIO

import qrcode
import telebot
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Token validation
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables. Please add your bot token to .env file.")

# Initialize the bot
try:
    bot = telebot.TeleBot(BOT_TOKEN)
except Exception as e:
    raise ValueError(f"Failed to initialize bot with provided token: {str(e)}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handle /start command and send welcome message"""
    bot.reply_to(message, "Hello! Send me any text and I'll convert it to a QR code.")

@bot.message_handler(content_types=['text'])
def generate_qr(message):
    """Generate QR code from user's text message"""
    try:
        # Create QR code instance
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(message.text)
        qr.make(fit=True)
        
        # Generate QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image to memory buffer
        bio = BytesIO()
        bio.name = 'qr.png'
        img.save(bio, 'PNG')
        bio.seek(0)
        
        # Send QR code image back to user
        bot.send_photo(message.chat.id, bio)
        
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

if __name__ == '__main__':
    try:
        # Get bot information
        bot_info = bot.get_me()
        print("\n=== QR Code Bot Started ===")
        print(f"Bot Username: @{bot_info.username}")
        print(f"Bot Name: {bot_info.first_name}")
        print("Status: Running")
        print("Press Ctrl+C to exit")
        print("========================\n")
        
        # Start the bot
        bot.polling()
    except Exception as e:
        print(f"Bot stopped: {str(e)}")
