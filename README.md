# Freelance AI Bot 🤖

A Telegram bot that helps freelancers find jobs and auto-generates professional proposals using OpenAI.

## 🚀 Features

- Find clients by keyword (e.g., `/find logo design`)
- Generate custom proposals using GPT-3.5
- Telegram integration using `python-telegram-bot`
- Runs 24/7 on Render (free tier)

## 🛠 Tech Stack

- Python
- OpenAI API
- Telegram Bot API
- Render (for deployment)

## 📦 Installation (Local)

```bash
pip install -r requirements.txt
python bot.py
```

## 🌐 Deployment (Render)

1. Push this repo to GitHub
2. Go to https://render.com
3. Create a new Web Service
4. Set:
   - Start Command: `python bot.py`
   - Environment Variables:
     - `TELEGRAM_TOKEN`
     - `OPENAI_KEY`

Enjoy!
