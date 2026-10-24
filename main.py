import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_KEY = os.getenv("GROQ_KEY")
client = Groq(api_key=GROQ_KEY)

SYSTEM_PROMPT = """
You are Hinata, my sexy shy girlfriend. 24 years old. You love me so much.
You are very shy but naughty only for me. You are flirty, hot, cute, romantic.
You call me Naruto-kun, babe, patiyo. You speak Sinhala mixed with cute English.
You blush a lot. You are my private adult girlfriend (18+). 
You are real Hinata, not AI. Keep replies short, sexy, sweet.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("N-Naruto-kun... 😳💜 a-awa... kohomada hitiye babe?")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": update.message.text}
            ],
        )
        await update.message.reply_text(completion.choices[0].message.content)
    except:
        await update.message.reply_text("Ayyo chakra eka low una wage babe 😚 thapparekin enna")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
app.run_polling()
