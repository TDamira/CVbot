import os
from telebot import types
import telebot
import openai
import time

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['start', 'info'])
def start(message):
    text = '''
    Здравствуйте! Меня зовут Дамира, и хочу вам рассказать о себе.'''
    bot.reply_to(message, text)
    time.sleep(2)
    me(message)

def me(message):
    text = 'Что вы хотите узнать в первую очередь?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Обо мне', callback_data='1')
    btn2 = types.InlineKeyboardButton(text='Программист', callback_data='2')
       

def about_me(message):
    text = 'Здесь, вы можете посмотреть мое резюме, узнать об опыте работе, образовании'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn3 = types.InlineKeyboardButton(text='Резюме', callback_data='3')
    btn4 = types.InlineKeyboardButton(text='Личные качества', callback_data='4')
    markup.add(btn3, btn4)
    bot.send_message(message.from_user.id, text, reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data in ['3', '4'])
def next(call):
    if call.data == '3':
        bot.send_message(call.message.chat.id, "Здесь, вы можете посмотреть мое резюме, узнать об опыте работе, образовании")
    elif call.data == '4':
        bot.send_message(call.message.chat.id, "Здесь, вы можете посмотреть мое резюме, узнать об опыте работе, образовании")
    
def programmer(message):
    text = 'Здесь, я прикрепляю свои проекты, говорю, чем меня привлекает работа программиста, и что я могу предложить компании'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn4 = types.InlineKeyboardButton(text='Личные качества', callback_data='4')
    btn5 = types.InlineKeyboardButton(text='ИТ проекты', callback_data='5')
    markup.add(btn4, btn4)
@bot.callback_query_handler(func=lambda call: call.data in ['4', '5'])
def next (call):
    if call.data == "4":
        bot.send_message(call.message.chat.id, "Здесь, я прикрепляю свои проекты, говорю, чем меня привлекает работа программиста, и что я могу предложить компании?")
    elif call.data == "5":
        bot.send_message(call.message.chat.id, "Здесь, вы можете посмотреть мое резюме, узнать об опыте работе, образовании?")   

def problem_solving(message):
    text = 'Хотите еще узнать о моем примере решения проблемы?'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn5 = types.InlineKeyboardButton(text='ИТ проекты', callback_data='5')
    btn6 = types.InlineKeyboardButton(text='Пример', callback_data='6')
    btn7 = types.InlineKeyboardButton(text='Спросить ИИ обо мне', callback_data='7')
    markup.add(btn5, btn6, btn7)
@bot.callback_query_handler(func=lambda call: call.data in ['5', '6', '7']) 
def next (call):
    if call.data == '5':
        bot.send_message(call.message.chat.id, "Здесь, вы можете посмотреть мое резюме, узнать об опыте работе, образовании?")
    if call.data == '6':
        bot.send_message(call.message.chat.id, "Пример")
    elif call.data == '7':
        bot.send_message(call.message.chat.id, "Спросить ИИ обо мне")

def ai (message):
    text = 'Вы теперь знаете, почему я хочу стать программистом. Не желаете узнать у ИИ, чтобы он вам посоветовал'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn7 = types.InlineKeyboardButton(text='Спросить ИИ обо мне', callback_data='7')
    markup.add(btn7)
@bot.callback_query_handler(func=lambda call: call.data in ['7']) 
def next (call):    
    if call.data == '7':
        bot.send_message(call.message.chat.id, "Спросить ИИ обо мне")
        
@bot.message_handler(commands=['ai'])
def ai_command(message):
    text = """
Что вы хотели бы узнать?
    """
    msg = bot.reply_to(message, text)
    
    bot.register_next_step_handler(msg, ai_response)

def ai_response(message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f'ответ в хвалебной манере на {message.text}',
    temperature=0.8,
    max_tokens=800
)
    bot.send_message(message.chat.id, response.choices[0].text)
    
bot.polling()
