import telebot
import random
Token = ''
bot = telebot.TeleBot(Token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")


need = ('rock', 'paper', 'scissors')


global game_current
games = {}
game_current = -1e9


@bot.message_handler(commands=['create'])
def constructor(message):
    game_id = message.text.split()[1]
    if len(games[game_id]) != 2:
        games[game_id] = set(message.from_user.id)
    else:
        bot.reply_to(message, 'Уже занято')

@bot.message_handler(commands=['join'])
def join(message):
    game_id = message.text.split()[1]
    game_current = game_id


@bot.message_handler(content_types=['text'])
def my_game(message):
    if message.text.lower() == 'my game':
        if game_current != -1e9:
            bot.send_message(message.chat_id, game_current)
        else:
            bot.send_message(message.chat_id, 'Ты не в игре')


@bot.message_handler(commands=['play'])
def play(message):
    if game_current != -1e9:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        itembtnRock = telebot.types.KeyboardButton('Rock')
        itembtnPaper = telebot.types.KeyboardButton('Paper')
        itembtnScissors = telebot.types.KeyboardButton('Scissors')
        markup.add(itembtnPaper, itembtnRock, itembtnScissors)
        chat_id = message.chat_id
        bot.send_message(chat_id, "Choose:", reply_markup=markup)


bot.polling(none_stop=True)
