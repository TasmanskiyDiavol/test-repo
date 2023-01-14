import telebot
from random import randint

bot = telebot.TeleBot(token="5889190596:AAFqytRL_dTyYMfZbPnnULWUNIall_yNNXQ")

@bot.message_handler(content_types=['text'])
def answer(message):
    global adress
    global filtr
    global opisanie
    text = message.text
    user = message.chat.id

    if text == "/start":
        bot.send_photo(user, "https://yandex.ru/images/search?from=tabbar&text=%D1%81%D0%BE%D0%B1%D0%B0%D1%87%D0%BA%D0%B0%20%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0&family=yes&pos=1&img_url=http%3A%2F%2Fadonius.club%2Fuploads%2Fposts%2F2022-06%2F1655597329_7-adonius-club-p-khobotkovaya-sobachka-krasivo-foto-7.jpg&rpt=simage&lr=213")
        bot.send_message(user, r"""Скопируйте и заполните анкету, не изменяя её, (в скобочках написан пример): 
:Адресс (ул. Пушкина, д.2): 
:Фильтры (#НазваниеФильтра): 
:Описание (Очень интересный квест много загадок): """)
    elif text[:29] == "Скопируйте и заполните анкету":
        bot.send_message(user, "Спасибо за информацию")
        bot.send_photo(user, "https://yandex.ru/images/search?text=%D0%BA%D0%B8%D1%82%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2&family=yes&from=tabbar&pos=0&rpt=simage&img_url=http%3A%2F%2Fgas-kvas.com%2Fuploads%2Fposts%2F2022-09%2F1663253619_1-gas-kvas-com-p-ptitsa-kitoglav-foto-1.jpg&lr=213")
        info = text.split(":")
        adress.append(info[3])
        filtr.append(info[5])
        opisanie.append(info[7])
        print(adress)
        print(filtr)
        print(opisanie)
    elif text == "/d":
        bot.send_message(user, ','.join(adress))
        bot.send_message(user, ','.join(filtr))
        bot.send_message(user, ','.join(opisanie))
#    else:
#        bot.send_message(user, text)
#        bot.send_photo(user, "https://funart.pro/uploads/posts/2021-07/1626378013_8-funart-pro-p-khobotkovaya-sobachka-petersa-zhivotnie-kr-9.jpg")
adress = []
filtr = []
opisanie = []
bot.polling(none_stop=True)

#ctaroe foto: https://funart.pro/uploads/posts/2021-07/1626378013_8-funart-pro-p-khobotkovaya-sobachka-petersa-zhivotnie-kr-9.jpg
