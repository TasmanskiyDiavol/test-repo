import telebot
from random import randint

bot = telebot.TeleBot(token="5889190596:AAFqytRL_dTyYMfZbPnnULWUNIall_yNNXQ")


@bot.message_handler(content_types=['text'])
def answer(message):
    global adress
    global filtr
    global opisanie
    global n
    global s
    text = message.text
    user = message.chat.id
    if text == "/help":
        bot.send_message(user, r"""Тебе нужна помощь?
/start - аполнить анкету нового места
/random - случайная локация""")

    elif text == "/start":
        bot.send_photo(user,
                       "https://yandex.ru/images/search?from=tabbar&text=%D1%81%D0%BE%D0%B1%D0%B0%D1%87%D0%BA%D0%B0%20%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0&family=yes&pos=1&img_url=http%3A%2F%2Fadonius.club%2Fuploads%2Fposts%2F2022-06%2F1655597329_7-adonius-club-p-khobotkovaya-sobachka-krasivo-foto-7.jpg&rpt=simage&lr=213")
        bot.send_message(user, r"""Скопируйте и заполните анкету, не изменяя её, (в скобочках написан пример): 
:Адресс (ул. Пушкина, д.2): 
:Фильтры (#НазваниеФильтра): 
:Описание (Очень интересный квест много загадок): """)
    elif text[:29] == "Скопируйте и заполните анкету":
        bot.send_message(user, "Спасибо за информацию")
        bot.send_photo(user,
                       "https://yandex.ru/images/search?text=%D0%BA%D0%B8%D1%82%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2&family=yes&from=tabbar&pos=0&rpt=simage&img_url=http%3A%2F%2Fgas-kvas.com%2Fuploads%2Fposts%2F2022-09%2F1663253619_1-gas-kvas-com-p-ptitsa-kitoglav-foto-1.jpg&lr=213")
        info = text.split(":")
        adress.append(info[3])
        filtr.append(info[5])
        opisanie.append(info[7])

#        with open("adress.txt", "w") as file_adress:
#            for i in adress:
#                file_adress.write("".join(i) + "\n")

#        with open("filtr.txt", "w") as file_filtr:
#            for i in filtr:
#                file_filtr.write("".join(i) + "\n")

#        with open("opisanie.txt", "w") as file_opisanie:
#            for i in opisanie:
#                file_opisanie.write("".join(i) + "\n")
        n = n + 1


    elif text == "/d":
        bot.send_message(user, ','.join(adress))
        bot.send_message(user, ','.join(filtr))
        bot.send_message(user, ','.join(opisanie))



    elif text == "/random":

        bot.send_photo(user,
                       "https://yandex.ru/images/search?from=tabbar&text=%D0%BF%D0%BE%D0%BB%D0%BE%D1%81%D0%B0%D1%82%D1%8B%D0%B9%20%D1%82%D0%B5%D0%BD%D1%80%D0%B5%D0%BA&family=yes&pos=0&img_url=http%3A%2F%2Fmnogo-krolikov.ru%2Fwp-content%2Fuploads%2F2021%2F01%2Fstriped-malagasy-tenrec.jpg.838x0_q80.jpg&rpt=simage&lr=213")

        a = randint(0, n - 1)
        a1 = adress[a]
        f1 = filtr[a]
        o1 = opisanie[a]
        a2 = "Адресс:" + a1
        f2 = "Указанные фильтры:" + f1
        o2 = "Описание:" + o1
        bot.send_message(user, a2)
        bot.send_message(user, f2)
        bot.send_message(user, o2)

n = 0
adress = []
filtr = []
opisanie = []
#with open("adress.txt", "r") as file_adress:
#    for i in file_adress:
#        adress.append(i.split(" "))
#with open("filtr.txt", "r") as file_filtr:
#    for i in file_filtr:
#        filtr.append(i.split(" "))
#with open("opisanie.txt", "r") as file_opisanie:
#    for i in file_opisanie:
#        opisanie.append(i.split(" "))
bot.polling(none_stop=True)

