import telebot
import requests

BOT_TOKEN = "8980443786:AAG0-WIQQEuztstX1m_1eXwfxPaAemyE14U"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def player_info(message):
    try:
        uid = message.text.split()[1]
        response = requests.get(f"http://localhost:5000/info?uid={uid}")
        data = response.json()
        msg = f"""
🎮 Player Info:
👤 Name: {data['basicInfo']['nickname']}
⭐ Level: {data['basicInfo']['level']}
🏆 Rank: {data['basicInfo']['rank']}
🌍 Region: {data['basicInfo']['region']}
        """
        bot.reply_to(message, msg)
    except:
        bot.reply_to(message, "❌ Sahi UID do!")

bot.polling()