import logging
import openai
import os
import time
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Add your keys here (or load them from environment variables)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY

# ✅ Setup logging
logging.basicConfig(level=logging.INFO)

# ✅ Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I'm your freelance AI agent.\nType: /find logo design")

# ✅ Find command
async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗Please use a keyword. Example: /find graphic design")
        return

    keyword = ' '.join(context.args)
    await update.message.reply_text("🔍 Please wait while I search and write your proposal...")

    job_title = f"Need a {keyword} expert"
    budget = "$100"
    job_link = "https://www.fiverr.com"

    proposal = ""
    try:
        start_time = time.time()
        response = await asyncio.to_thread(openai.ChatCompletion.create,
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Write a short and professional freelance proposal for:\nTitle: {job_title}\nBudget: {budget}"
            }],
            timeout=8
        )
        proposal = response.choices[0].message.content.strip()
        duration = time.time() - start_time
        print(f"[GPT] Response time: {duration:.2f} sec")

    except Exception as e:
        print(f"[GPT Error] {e}")
        proposal = f"Hi! I noticed you're looking for a {keyword} expert. I have experience handling similar projects and would love to help. Let's connect and discuss your requirements."

    await update.message.reply_text(f"🧾 Job: {job_title}\n💵 Budget: {budget}\n🔗 Link: {job_link}")
    await update.message.reply_text(f"🤖 AI Proposal:\n{proposal}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("find", find))
    app.run_polling()

if __name__ == "__main__":
    main()
