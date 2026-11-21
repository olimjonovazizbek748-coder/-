import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎭 Shadow Mafia Bot ishga tushdi! O‘yinni boshlash uchun meni guruhga qo‘shing va admin qiling.")

@bot.message_handler(commands=['game'])
def new_game(message):
    if message.chat.type in ['group', 'supergroup']:
        bot.send_message(message.chat.id, "🕵️‍♂️ Yangi Mafia o‘yini uchun ro‘yxatga olish boshlandi! Qo‘shilish uchun /join yozing.")
    else:
        bot.reply_to(message, "❌ Bu buyruq faqat guruhlarda ishlaydi!")

print("Bot ishlamoqda...")
bot.infinity_polling()
