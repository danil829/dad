from telebot import TeleBot
from model import init, get_placement
import time
init_world, world_dict = init()
similarities = []
TOKEN = '6642468718:AAFLbN7L6_gMd_iDufD9E6U9L6pvb7U4H38'
bot = TeleBot(TOKEN)

print(len(world_dict))
print(init_world)

def get_string_words(similarities):
    end_string = ''
    for sim, count in similarities:
        end_string += f'{sim}{count}\n'
    return end_string


@bot.message_handler(commands=['start'])
def start():
    bot.send_message(message.chat.id, 'ВВодите любые слова, чтобы играть. Используйте команду word')
@bot.message_handler(commands=['word'])
def word(message):
    global similarities
    if len(message.text.split(' '))> 2:
        bot.send_message(message.chat.id, 'Больше одного слова нельзя')
        return
    _, word = message.text.split(' ')
    if word == init_world:
        bot.send_message(message.chat.id, 'Правильно')
        return
    place = get_placement(word, world_dict)
    if place == -1:
        bot.send_message(message.chat.id, 'Очень далеко')
        return
    try:
        similarities.append((word,place))
        similarities.sort(key=lambda tup: tup[1])
        msg = get_string_words(similarities)
        bot.send_message(message.chat.id, msg)
    except Exception as e:
        print(f'Exception occured:{type(e).__name__}:{e}')
        print('Attempting to resend message in 10 seconds...')
        time.sleep(3)
        word(message)
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f'Exception occured:{type(e).__name__}:{e}')
            print('Attempting to resend message in 10 seconds...')
            time.sleep(3)
            