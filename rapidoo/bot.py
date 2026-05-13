import telebot

TOKEN = "8573362410:AAGv6JAXQXvXOHF_dt6cbgCPkjMvrTL9qW8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Send number like:\n/check 9876543210")

@bot.message_handler(commands=['check'])
def check(message):
    try:
        number = message.text.split()[1]

        # Dummy logic
        if number.endswith("5"):
            result = "OLD Number"
        else:
            result = "NEW Number"

        bot.reply_to(message, f"""
Number: {number}

Status: {result}
""")

    except:
        bot.reply_to(message, "Use:\n/check 9876543210")

print("Bot Running...")
bot.infinity_polling()