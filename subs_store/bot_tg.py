from sqlalchemy import update, select
from sqlalchemy.orm import Session
from telebot import types, TeleBot

from tg_bots.alh_models import engine, CustomUser

BOT_TOKEN = '8021634320:AAE0nSYrc6Ou5UIS9u8hOpuXw8tTFgEjB-A'

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup()
    reg_button = types.KeyboardButton(text="Подключить уведомления")
    keyboard.add(reg_button)

    sent = bot.send_message(message.chat.id,
                        f'Привет, я позаимствую твой id: {message.from_user.id}',
                        reply_markup=keyboard)
    bot.register_next_step_handler(sent, get_phone)

def get_phone(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg_button = types.KeyboardButton(text="Отправить номер телефона",
                                      request_contact=True)
    keyboard.add(reg_button)
    ph = bot.send_message(message.chat.id,
                     "Оставьте ваш контактный номер, " +
                     "чтобы мы могли уведомлять Вас о новых заказах.",
                     reply_markup=keyboard)
    bot.register_next_step_handler(ph, message_phone)

def message_phone(message):
    bot.send_message(message.chat.id, f'Спасибо за номер телефона: {message.contact.phone_number}.' +
                                      f' Телеграмм ID привязан к аккаунту сайта')

    stmt = (
        update(CustomUser)
        .where(CustomUser.phone == message.contact.phone_number)
        .values(tg_id=message.from_user.id)
    )

    with Session(engine) as session:
        session.execute(stmt)
        session.commit()



def notification_for_user(username):
    session = Session(engine)
    stmt = select(CustomUser).where(CustomUser.username == username)
    result = session.scalars(stmt).one()
    bot.send_message(result.tg_id, f"Ваш заказ успешно создан. Спасибо!")




if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)