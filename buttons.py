from telebot import types

# Кнопка для отправки номера
def num_bt():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    number = types.KeyboardButton('☎️ Отправить номер', request_contact=True)

    kb.add(number)
    return kb

# Кнопка для отправки локации
def loc_bt():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    location = types.KeyboardButton('📍 Отправить локацию', request_location=True)

    kb.add(location)
    return kb

