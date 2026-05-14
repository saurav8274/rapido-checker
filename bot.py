import telebot
from telebot import types
import time

# =========================
# BOT TOKEN
# =========================
TOKEN = "8573362410:AAGv6JAXQXvXOHF_dt6cbgCPkjMvrTL9qW8"

bot = telebot.TeleBot(TOKEN)

# =========================
# START COMMAND
# =========================
@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup(row_width=1)

    btn1 = types.InlineKeyboardButton(
        "📱 CHECK NUMBER",
        callback_data="check"
    )

    btn2 = types.InlineKeyboardButton(
        "👑 PREMIUM ACCESS",
        callback_data="premium"
    )

    btn3 = types.InlineKeyboardButton(
        "📢 UPDATE CHANNEL",
        url="https://t.me/yourchannel"
    )

    btn4 = types.InlineKeyboardButton(
        "🛠 HELP CENTER",
        callback_data="help"
    )

    markup.add(btn1, btn2, btn3, btn4)

    welcome = f"""
👋 𝗛𝗘𝗬 {message.from_user.first_name}!

💰 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗥𝗔𝗣𝗜𝗗𝗢 𝗖𝗛𝗘𝗖𝗞𝗘𝗥

⚡ 𝗙𝗔𝗦𝗧 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘
🌐 𝗢𝗡𝗟𝗜𝗡𝗘 24/7
🔒 𝗦𝗘𝗖𝗨𝗥𝗘 𝗖𝗛𝗘𝗖𝗞𝗘𝗥

👉 𝗖𝗛𝗢𝗢𝗦𝗘 𝗬𝗢𝗨𝗥 𝗢𝗣𝗧𝗜𝗢𝗡 𝗕𝗘𝗟𝗢𝗪
"""

    bot.send_message(
        message.chat.id,
        welcome,
        reply_markup=markup
    )

# =========================
# BUTTON HANDLER
# =========================
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "check":

        bot.send_message(
            call.message.chat.id,
            "📲 SEND NUMBER\n\nExample:\n/check 9876543210"
        )

    elif call.data == "premium":

        bot.send_message(
            call.message.chat.id,
            "👑 PREMIUM VERSION\n\n⚡ Faster Checking\n📂 Bulk Checker\n🛡 Advanced Access"
        )

    elif call.data == "help":

        bot.send_message(
            call.message.chat.id,
            "🛠 HELP CENTER\n\nUse command:\n/check 9876543210"
        )

# =========================
# CHECK COMMAND
# =========================
@bot.message_handler(commands=['check'])
def check(message):

    try:

        number = message.text.split()[1]

        # =========================
        # VALIDATION
        # =========================
        if not number.isdigit():
            bot.reply_to(message, "❌ Only numbers allowed")
            return

        if len(number) != 10:
            bot.reply_to(message, "❌ Enter valid 10 digit number")
            return

        # =========================
        # LOADING EFFECT
        # =========================
        loading = bot.reply_to(
            message,
            "⏳ CHECKING NUMBER..."
        )

        time.sleep(2)

        # =========================
        # DEMO CHECKER LOGIC
        # =========================
        if number.endswith("0"):
            result = "NEW"
            emoji = "🆕"

        else:
            result = "OLD"
            emoji = "♻️"

        # =========================
        # FINAL RESULT
        # =========================
        final_text = f"""
╔══════════════════╗
   RAPIDO CHECKER
╚══════════════════╝

📱 NUMBER: {number}

📊 STATUS: {emoji} {result}

⚡ CHECKED SUCCESSFULLY
"""

        bot.edit_message_text(
            final_text,
            chat_id=message.chat.id,
            message_id=loading.message_id
        )

    except:

        bot.reply_to(
            message,
            "❌ USE:\n/check 9876543210"
        )

# =========================
# UNKNOWN MESSAGE HANDLER
# =========================
@bot.message_handler(func=lambda message: True)
def unknown(message):

    bot.reply_to(
        message,
        "❌ INVALID COMMAND\nUse /start"
    )

# =========================
# RUN BOT
# =========================
print("🔥 Premium Bot Running...")
bot.infinity_polling()
