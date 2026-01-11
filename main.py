import telebot
from telebot import types

TOKEN = '8225048686:AAFIWvGg9ye6VfZX8v0xIMfehBdu5wcNYg8'
LOGO_FILE_ID = 'AgACAgQAAxkBAAMEaWQDqEAcr80AASb-FRQz4-g7DqpwAAINDGsbjcYhU0EM35qIIx2yAQADAgADeQADOAQ'

bot = telebot.TeleBot(TOKEN)

LINKS = {
    "2007": "https://t.me/+lUmbHfVBz5A4MzBk", "2008": "https://t.me/+ZzDYKPY9TshlZWI8",
    "2009": "https://t.me/+sG_NfrM4JhllZTk8", "2010": "https://t.me/+O_qSb4_pOUUwZWY0",
    "2011": "https://t.me/+h3lYPBqa1SE3YzM8", "2012": "https://t.me/+RtdQfSuuaxo0MDQ0",
    "2013": "https://t.me/+XgG0F8zJKsA1OWRk", "2014": "https://t.me/+Y66FteBWy9AzNWRk",
    "2015": "https://t.me/+15DfEOWfmt43NzBk", "2016": "https://t.me/+FAynAxR3u9ZkNGVk",
    "2017": "https://t.me/+I2ok1rRfIhIzZGNk"
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📂 የትዝታ ማህደር', '🎭 ድራማና ስነ-ጽሁፍ', '🗓 ፕሮግራሞች', '🏠 ስለ ህብረቱ')
    bot.send_photo(message.chat.id, LOGO_FILE_ID, caption="ሰላም! እንኳን ወደ ሩሀማ ህብረት ቦት በሰላም መጡ።", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📂 የትዝታ ማህደር')
def archive(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    btns = [types.InlineKeyboardButton(f"📅 {y}", callback_data=f"lnk_{y}") for y in LINKS.keys()]
    markup.add(*btns)
    bot.send_message(message.chat.id, "የሚፈልጉትን ዓመት ይምረጡ፦", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.startswith('lnk_'):
        year = call.data.split('_')[1]
        url = LINKS.get(year)
        markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(f"ወደ {year} ማህደር ሂድ", url=url))
        bot.send_message(call.message.chat.id, f"የ{year} ማህደር ሊንክ፦", reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
  
