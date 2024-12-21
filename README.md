# QR Code Generator Bot

A Telegram bot that generates QR codes from text messages.

## Features

- Converts text messages to QR codes
- Simple and easy to use
- Instant QR code generation

## Requirements

```bash
pip install -r requirements.txt
```

## Setup

### Option 1: Local Setup

1. Clone this repository
```bash
git clone <repository-url>
cd qr-code-bot
```

2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  
# On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your bot token:
```plaintext
BOT_TOKEN=your_bot_token_here
```

5. Run the bot
```bash
python app.py
```

### Option 2: Docker Setup

1. Clone this repository
```bash
git clone <repository-url>
cd qr-code-bot
```

2. Create a `.env` file in the root directory and add your bot token:
```plaintext
BOT_TOKEN=your_bot_token_here
```

3. Build and run with Docker Compose
```bash
docker-compose up -d --build
```

To stop the bot:
```bash
docker-compose down
```

## How to Get a Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Start a chat and send `/newbot`
3. Follow the instructions to create a new bot
4. Copy the token provided and add it to your `.env` file

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to get the welcome message
3. Send any text message
4. Receive the QR code image

## Docker Commands

Common Docker commands for managing the bot:

- View logs: `docker-compose logs -f`
- Restart the bot: `docker-compose restart`
- Stop the bot: `docker-compose down`
- Start the bot: `docker-compose up -d`
- Rebuild and start: `docker-compose up -d --build`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
